from pathlib import Path
import re
import subprocess
import sys

try:
    import numpy as np
    import pandas as pd
    from rank_bm25 import BM25Okapi
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError as exc:
    print("Missing dependency:", exc)
    print("Install with: pip install rank-bm25 sentence-transformers scikit-learn pandas numpy")
    raise SystemExit(1)

OUT = Path(__file__).resolve().parents[1] / "outputs"
REQ = OUT / "requirements.csv"
if not REQ.exists():
    subprocess.run([sys.executable, str(Path(__file__).with_name("requirements_dataset.py"))], check=True)

def tok(text):
    return re.findall(r"0x[0-9A-Fa-f]+|[A-Za-z_]+|\d+", text.lower())

df = pd.read_csv(REQ)
corpus = [tok(t) for t in df["text"]]
bm25 = BM25Okapi(corpus)

try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception as exc:
    print("Could not load sentence-transformers model. First run may require internet/cache.")
    print("Error:", exc)
    raise SystemExit(1)

dense = model.encode(df["text"].tolist(), normalize_embeddings=True)
queries = [
    "unsupported DID returns NRC 0x31",
    "periodic CAN frame every 10 ms",
    "diagnostic request over DoIP TCP connection",
]

for q in queries:
    print(f"\nQUERY: {q}")
    bm_scores = bm25.get_scores(tok(q))
    q_emb = model.encode([q], normalize_embeddings=True)
    dense_scores = cosine_similarity(q_emb, dense)[0]
    bm_norm = (bm_scores - bm_scores.min()) / (bm_scores.max() - bm_scores.min() + 1e-9)
    dense_norm = (dense_scores - dense_scores.min()) / (dense_scores.max() - dense_scores.min() + 1e-9)
    for alpha in [0.3, 0.5, 0.7, 0.9]:
        hybrid = alpha * dense_norm + (1 - alpha) * bm_norm
        order = np.argsort(-hybrid)[:3]
        print(f" alpha={alpha}")
        for idx in order:
            print(f"  {df.loc[idx,'requirement_id']} score={hybrid[idx]:.3f} dense={dense_norm[idx]:.3f} bm25={bm_norm[idx]:.3f} {df.loc[idx,'text']}")
