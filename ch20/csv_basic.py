import csv
from pathlib import Path

path = Path(__file__).parent / "output" / "orders.csv"
path.parent.mkdir(exist_ok=True)

rows = [
    ["상품", "가격", "메모"],
    ["키보드", 89000, "무선, 텐키리스"],
    ["마우스", 35000, ""],
]
with open(path, "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(rows)

print(path.read_text(encoding="utf-8"), end="")

with open(path, encoding="utf-8", newline="") as f:
    for row in csv.reader(f):
        print(row)
