from pathlib import Path

BASE = Path(__file__).parent.parent
backup_dir = BASE / "output" / "backup"
backup_dir.mkdir(parents=True, exist_ok=True)   # 중간 폴더까지 만든다

for source in sorted((BASE / "data").glob("*.txt")):
    target = backup_dir / f"{source.stem}_backup{source.suffix}"
    target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"{source.name} -> {target.name} ({target.stat().st_size}바이트)")
