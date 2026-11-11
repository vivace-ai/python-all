from pathlib import Path

BASE = Path(__file__).parent.parent
source = BASE / "data" / "access.log"
target = BASE / "output" / "errors.log"
target.parent.mkdir(exist_ok=True)

count = 0
with (
    open(source, encoding="utf-8") as src,
    open(target, "w", encoding="utf-8") as dst,
):
    for line in src:
        if " ERROR " in line:
            dst.write(line)
            count += 1

print(f"ERROR {count}건을 {target.name}에 저장했습니다.")
print(target.read_text(encoding="utf-8"), end="")
