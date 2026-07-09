from pathlib import Path
import csv

OUT = Path(__file__).resolve().parents[1] / "outputs"
REQ = OUT / "requirements.csv"
TESTS = OUT / "tests.csv"

if not REQ.exists() or not TESTS.exists():
    print("Missing CSV files. Run: python 13_Labs/code/requirements_dataset.py")
    raise SystemExit(1)

with REQ.open(encoding="utf-8") as f:
    requirements = list(csv.DictReader(f))
with TESTS.open(encoding="utf-8") as f:
    tests = list(csv.DictReader(f))

covered = {t["covers"] for t in tests if t.get("covers")}
print("Coverage by requirement:")
for r in requirements:
    status = "COVERED" if r["requirement_id"] in covered else "GAP"
    print(f"{r['requirement_id']:12} {r['module']:12} {status:8} {r['text']}")

coverage = len(covered & {r["requirement_id"] for r in requirements}) / len(requirements)
print(f"\nCoverage: {coverage:.1%}")
