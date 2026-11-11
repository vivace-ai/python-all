from pathlib import Path

BASE = Path(__file__).parent.parent
source = BASE / "data" / "notes.txt"
target = BASE / "output" / "numbered.txt"
target.parent.mkdir(exist_ok=True)

with (
    open(source, encoding="utf-8") as src,
    open(target, "w", encoding="utf-8") as dst,
):
    for number, line in enumerate(src, start=1):
        dst.write(f"{number:>2}: {line}")   # line 끝에 줄바꿈이 이미 있다

print(target.read_text(encoding="utf-8"), end="")
