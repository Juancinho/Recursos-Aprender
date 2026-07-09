from pathlib import Path
import subprocess
import sys

try:
    import pandas as pd
    from sentence_transformers import SentenceTransformer
    from qdrant_client import QdrantClient
    from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
except ImportError as exc:
    print("Missing dependency:", exc)
    print("Install with: pip install qdrant-client sentence-transformers pandas")
    raise SystemExit(1)

OUT = Path(__file__).resolve().parents[1] / "outputs"
REQ = OUT / "requirements.csv"
if not REQ.exists():
    subprocess.run([sys.executable, str(Path(__file__).with_name("requirements_dataset.py"))], check=True)

try:
    client = QdrantClient(url="http://localhost:6333", timeout=5)
    client.get_collections()
except Exception as exc:
    print("Could not connect to Qdrant at http://localhost:6333")
    print("Start it with: docker run -p 6333:6333 -v qdrant_data:/qdrant/storage qdrant/qdrant:latest")
    print("Error:", exc)
    raise SystemExit(1)

df = pd.read_csv(REQ)
try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception as exc:
    print("Could not load sentence-transformers model. First run may require internet/cache.")
    print("Error:", exc)
    raise SystemExit(1)

vectors = model.encode(df["text"].tolist(), normalize_embeddings=True)
collection = "requirements"
dim = len(vectors[0])

if not client.collection_exists(collection):
    client.create_collection(collection, vectors_config=VectorParams(size=dim, distance=Distance.COSINE))
    print(f"Created collection {collection}")

points = [
    PointStruct(
        id=i,
        vector=vectors[i].tolist(),
        payload={
            "requirement_id": row.requirement_id,
            "module": row.module,
            "text": row.text,
        },
    )
    for i, row in df.iterrows()
]
client.upsert(collection_name=collection, points=points)
print(f"Upserted {len(points)} points")

query = "unsupported DID should return negative response code"
qv = model.encode([query], normalize_embeddings=True)[0].tolist()
print(f"\nSearch: {query}")
hits = client.query_points(collection_name=collection, query=qv, limit=5).points
for h in hits:
    print(f"{h.score:.3f} {h.payload['requirement_id']} {h.payload['module']} {h.payload['text']}")

print("\nFiltered search: module == diagnostics")
flt = Filter(must=[FieldCondition(key="module", match=MatchValue(value="diagnostics"))])
hits = client.query_points(collection_name=collection, query=qv, query_filter=flt, limit=5).points
for h in hits:
    print(f"{h.score:.3f} {h.payload['requirement_id']} {h.payload['module']} {h.payload['text']}")
