import argparse
import ast
from pathlib import Path

try:
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError as exc:
    print("Missing dependency:", exc)
    print("Install with: pip install sentence-transformers scikit-learn numpy")
    raise SystemExit(1)

def extract_symbols(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
        tree = ast.parse(text)
    except Exception:
        return []
    lines = text.splitlines()
    chunks = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            start = getattr(node, "lineno", 1)
            end = getattr(node, "end_lineno", start)
            code = "\n".join(lines[start - 1:end])
            chunks.append({
                "file_path": str(path),
                "symbol": node.name,
                "start_line": start,
                "end_line": end,
                "language": "python",
                "text": code,
            })
    return chunks

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".", help="Repository path to index")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    chunks = []
    for path in repo.rglob("*.py"):
        if any(part in {".git", ".venv", "venv", "__pycache__"} for part in path.parts):
            continue
        chunks.extend(extract_symbols(path))
    if not chunks:
        print("No Python functions/classes found.")
        return
    try:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    except Exception as exc:
        print("Could not load sentence-transformers model. First run may require internet/cache.")
        print("Error:", exc)
        raise SystemExit(1)
    texts = [c["symbol"] + "\n" + c["text"] for c in chunks]
    emb = model.encode(texts, normalize_embeddings=True)
    queries = ["where is vector search implemented?", "code that applies a patch", "function that calculates coverage"]
    for q in queries:
        qv = model.encode([q], normalize_embeddings=True)
        scores = cosine_similarity(qv, emb)[0]
        order = np.argsort(-scores)[:5]
        print(f"\nQUERY: {q}")
        for idx in order:
            c = chunks[idx]
            print(f"{scores[idx]:.3f} {c['file_path']}:{c['start_line']} {c['symbol']}")

if __name__ == "__main__":
    main()
