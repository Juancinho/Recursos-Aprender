"""
Build a small requirement graph using candidate retrieval + token-level attention.

This is a didactic implementation. In a production system with hundreds/thousands of
requirements, candidate generation should normally use Qdrant/BM25/hybrid search.
The attention score here is an interpretable unsupervised alignment signal, not a
validated classifier.
"""
from pathlib import Path
import csv
import hashlib
import math
import re

try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as exc:
    print("Missing dependency:", exc)
    print("Install with: pip install numpy pandas matplotlib")
    raise SystemExit(1)

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import PCA
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

try:
    import networkx as nx
    NETWORKX_AVAILABLE = True
except ImportError:
    NETWORKX_AVAILABLE = False


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
REQ_PATH = OUT / "requirements.csv"
NODES_PATH = OUT / "requirements_graph_nodes.csv"
EDGES_PATH = OUT / "requirements_graph_edges.csv"
PLOT_PATH = OUT / "requirements_graph.png"


DEFAULT_REQUIREMENTS = [
    ("REQ-UDS-001", "diagnostics", "The ECU shall support UDS service 0x22 ReadDataByIdentifier."),
    ("REQ-UDS-002", "diagnostics", "The diagnostic module shall return NRC 0x31 when the DID is unsupported."),
    ("REQ-UDS-003", "diagnostics", "The ECU shall respond with positive response 0x62 for a supported DID."),
    ("REQ-UDS-004", "diagnostics", "Unsupported diagnostic identifiers shall be rejected with request out of range."),
    ("REQ-CAN-001", "can", "The body controller shall transmit status frame 0x120 every 10 ms."),
    ("REQ-CAN-002", "can", "The gateway shall reject CAN frames with invalid DLC."),
    ("REQ-CAN-003", "can", "The status CAN frame 0x120 shall contain door lock state in byte 2."),
    ("REQ-DOIP-001", "doip", "The tester shall establish a DoIP TCP connection before diagnostic requests."),
    ("REQ-DOIP-002", "doip", "The gateway shall accept DoIP routing activation before UDS messages."),
    ("REQ-LGT-001", "lighting", "The vehicle shall turn on low beam when ambient light is below threshold."),
    ("REQ-LGT-002", "lighting", "The lighting controller shall switch off low beam when ambient light is above threshold."),
    ("REQ-BODY-001", "body", "The central locking system shall unlock all doors after a valid remote command."),
]


def ensure_requirements_csv():
    if REQ_PATH.exists():
        return
    with REQ_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["requirement_id", "module", "text"])
        writer.writerows(DEFAULT_REQUIREMENTS)
    print(f"Created synthetic dataset: {REQ_PATH}")


def tokenize(text):
    return [t.lower() for t in re.findall(r"0x[0-9a-fA-F]+|[a-zA-Z_]+|\d+", text)]


def stable_token_vector(token, dim=48):
    """Deterministic pseudo-embedding for a token.

    This keeps the lab self-contained. Replace this with contextual token
    embeddings from a Transformer if you need semantic attention.
    """
    digest = hashlib.sha256(token.encode("utf-8")).digest()
    seed = int.from_bytes(digest[:8], "little", signed=False)
    rng = np.random.default_rng(seed)
    vec = rng.normal(size=dim)
    norm = np.linalg.norm(vec) or 1.0
    return vec / norm


def lexical_bonus(a, b):
    """Give technical exact matches a stronger alignment signal."""
    if a == b:
        return 1.0
    technical = ("0x", "uds", "did", "nrc", "can", "doip", "dlc", "ecu")
    if a in technical and b in technical:
        return 0.25
    if a.startswith("0x") and b.startswith("0x"):
        return 0.20
    return 0.0


def cross_attention_alignment(tokens_a, tokens_b):
    """Return attention matrix and summary score for A attending to B."""
    if not tokens_a or not tokens_b:
        return np.zeros((len(tokens_a), len(tokens_b))), 0.0

    A = np.vstack([stable_token_vector(t) for t in tokens_a])
    B = np.vstack([stable_token_vector(t) for t in tokens_b])
    scores = A @ B.T / math.sqrt(A.shape[1])

    for i, ta in enumerate(tokens_a):
        for j, tb in enumerate(tokens_b):
            scores[i, j] += lexical_bonus(ta, tb)

    scores = scores - scores.max(axis=1, keepdims=True)
    exp_scores = np.exp(scores)
    attn = exp_scores / exp_scores.sum(axis=1, keepdims=True)
    row_max = attn.max(axis=1)
    return attn, float(row_max.mean())


def top_evidence(tokens_a, tokens_b, attn, n=5):
    pairs = []
    for i, ta in enumerate(tokens_a):
        for j, tb in enumerate(tokens_b):
            if ta in {"the", "shall", "a", "an", "is", "be", "with", "when"}:
                continue
            if tb in {"the", "shall", "a", "an", "is", "be", "with", "when"}:
                continue
            pairs.append((float(attn[i, j]), ta, tb))
    pairs.sort(reverse=True)
    return "; ".join(f"{a}->{b}:{score:.2f}" for score, a, b in pairs[:n])


def candidate_similarity(texts):
    if SKLEARN_AVAILABLE:
        vectorizer = TfidfVectorizer(token_pattern=r"0x[0-9A-Fa-f]+|[A-Za-z_]+|\d+", lowercase=True)
        X = vectorizer.fit_transform(texts)
        sim = (X @ X.T).toarray()
        return sim, X.toarray()

    token_sets = [set(tokenize(t)) for t in texts]
    n = len(texts)
    sim = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            union = token_sets[i] | token_sets[j]
            sim[i, j] = len(token_sets[i] & token_sets[j]) / len(union) if union else 0.0
    features = np.eye(n)
    print("scikit-learn not installed; using simple Jaccard fallback.")
    print("For TF-IDF + PCA install: pip install scikit-learn")
    return sim, features


def build_graph(df, top_k=3, min_weight=0.22):
    texts = df["text"].tolist()
    sim, features = candidate_similarity(texts)
    edges = []
    seen = set()

    for i, row in df.iterrows():
        candidates = np.argsort(sim[i])[::-1]
        kept = 0
        for j in candidates:
            if i == j:
                continue
            key = tuple(sorted((int(i), int(j))))
            if key in seen:
                continue
            if kept >= top_k:
                break
            seen.add(key)
            kept += 1

            tokens_a = tokenize(df.loc[i, "text"])
            tokens_b = tokenize(df.loc[j, "text"])
            attn_ab, score_ab = cross_attention_alignment(tokens_a, tokens_b)
            attn_ba, score_ba = cross_attention_alignment(tokens_b, tokens_a)
            attention_score = (score_ab + score_ba) / 2.0
            candidate_score = float(sim[i, j])
            weight = 0.6 * candidate_score + 0.4 * attention_score

            if weight < min_weight:
                continue

            evidence_ab = top_evidence(tokens_a, tokens_b, attn_ab, n=3)
            evidence_ba = top_evidence(tokens_b, tokens_a, attn_ba, n=2)
            relation_hint = "same_module" if df.loc[i, "module"] == df.loc[j, "module"] else "cross_module"

            edges.append({
                "source": df.loc[i, "requirement_id"],
                "target": df.loc[j, "requirement_id"],
                "source_module": df.loc[i, "module"],
                "target_module": df.loc[j, "module"],
                "candidate_score": round(candidate_score, 4),
                "attention_score": round(attention_score, 4),
                "weight": round(weight, 4),
                "relation_hint": relation_hint,
                "evidence": evidence_ab + " | reverse: " + evidence_ba,
            })

    return pd.DataFrame(edges), features


def save_nodes(df, features):
    nodes = df[["requirement_id", "module", "text"]].copy()
    if SKLEARN_AVAILABLE and len(df) >= 2:
        pca = PCA(n_components=2, random_state=42)
        coords = pca.fit_transform(features)
        nodes["x"] = coords[:, 0]
        nodes["y"] = coords[:, 1]
    else:
        angles = np.linspace(0, 2 * math.pi, len(df), endpoint=False)
        nodes["x"] = np.cos(angles)
        nodes["y"] = np.sin(angles)
    nodes.to_csv(NODES_PATH, index=False)
    return nodes


def plot_graph(nodes, edges):
    plt.figure(figsize=(11, 8))

    if NETWORKX_AVAILABLE and not edges.empty:
        graph = nx.Graph()
        for _, node in nodes.iterrows():
            graph.add_node(node["requirement_id"], module=node["module"])
        for _, edge in edges.iterrows():
            graph.add_edge(edge["source"], edge["target"], weight=edge["weight"])

        pos = {row["requirement_id"]: (row["x"], row["y"]) for _, row in nodes.iterrows()}
        widths = [1.0 + 4.0 * graph[u][v]["weight"] for u, v in graph.edges()]
        nx.draw_networkx_edges(graph, pos, width=widths, alpha=0.45)
        nx.draw_networkx_nodes(graph, pos, node_size=900, node_color="#dceafe", edgecolors="#2f4f7f")
        nx.draw_networkx_labels(graph, pos, font_size=8)
    else:
        plt.scatter(nodes["x"], nodes["y"], s=220)
        for _, row in nodes.iterrows():
            plt.text(row["x"], row["y"], row["requirement_id"], fontsize=8)
        if not NETWORKX_AVAILABLE:
            print("networkx not installed; saved PCA/scatter visualization only.")
            print("Install with: pip install networkx")

    plt.title("Requirement graph: candidate retrieval + token attention")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(PLOT_PATH, dpi=160)
    plt.close()


def main():
    ensure_requirements_csv()
    df = pd.read_csv(REQ_PATH)
    required = {"requirement_id", "module", "text"}
    missing = required - set(df.columns)
    if missing:
        print(f"{REQ_PATH} is missing columns: {sorted(missing)}")
        raise SystemExit(1)

    edges, features = build_graph(df, top_k=3, min_weight=0.22)
    nodes = save_nodes(df, features)
    edges.to_csv(EDGES_PATH, index=False)
    plot_graph(nodes, edges)

    print(f"Saved nodes: {NODES_PATH}")
    print(f"Saved edges: {EDGES_PATH}")
    print(f"Saved plot:  {PLOT_PATH}")
    if not edges.empty:
        print("\nTop edges:")
        print(edges.sort_values("weight", ascending=False).head(10).to_string(index=False))
    else:
        print("No edges passed the threshold. Lower min_weight or increase top_k.")


if __name__ == "__main__":
    main()

