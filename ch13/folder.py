from pathlib import Path

data = Path(__file__).parent / "data"

for path in sorted(data.iterdir()):     # 폴더 바로 아래의 항목
    kind = "폴더" if path.is_dir() else "파일"
    print(kind, path.name)

# glob()은 이 폴더에서만, rglob()은 하위 폴더까지 찾는다
print([p.name for p in sorted(data.glob("*.txt"))])
print([p.name for p in sorted(data.rglob("*.txt"))])
