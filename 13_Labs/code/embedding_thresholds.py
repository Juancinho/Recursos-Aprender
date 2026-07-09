from pathlib import Path
import csv
import subprocess
import sys

try:
    import numpy as np
    import pandas as pd
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError as exc:
    print("Missing dependency:", exc)
    print("Install with: pip install sentence-transformers scikit-learn pandas numpy")
    raise SystemExit(1)

OUT = Path(__file__).resolve().parents[1] / "outputs"
REQ = OUT / "requirements.csv"

if not REQ.exists():
    subprocess.run([sys.executable, str(Path(__file__).with_name("requirements_dataset.py"))], check=True)

df = pd.read_csv(REQ)
try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception as exc:
    print("Could not load sentence-transformers model. First run may require internet/cache.")
    print("Error:", exc)
    raise SystemExit(1)

emb = model.encode(df["text"].tolist(), normalize_embeddings=True)
sim = cosine_similarity(emb)

print("Top-k similar requirements:")
for i, row in df.iterrows():
    order = np.argsort(-sim[i])
    print(f"\n{row.requirement_id}: {row.text}")
    for j in order[1:4]:
        print(f"  {df.loc[j, 'requirement_id']} score={sim[i,j]:.3f} text={df.loc[j, 'text']}")

print("\nThreshold exploration:")
for th in [0.5, 0.6, 0.7, 0.8, 0.9]:
    pairs = []
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            if sim[i, j] >= th:
                pairs.append((df.loc[i, "requirement_id"], df.loc[j, "requirement_id"], sim[i, j]))
    print(f"threshold={th:.1f}: {len(pairs)} candidate pairs")
    for a, b, s in pairs[:5]:
        print(f"  possible FP/FN review: {a} - {b}: {s:.3f}")
