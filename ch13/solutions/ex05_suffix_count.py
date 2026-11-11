from pathlib import Path

data = Path(__file__).parent.parent / "data"

counts = {}
for path in data.rglob("*"):
    if path.is_file():
        counts[path.suffix] = counts.get(path.suffix, 0) + 1

for suffix in sorted(counts):
    print(suffix, counts[suffix])
