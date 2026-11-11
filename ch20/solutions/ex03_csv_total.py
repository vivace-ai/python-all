import csv
from pathlib import Path

path = Path(__file__).parent.parent / "data" / "sales.csv"

totals: dict[str, int] = {}
with open(path, encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        amount = int(row["price"]) * int(row["count"])
        totals[row["category"]] = totals.get(row["category"], 0) + amount

for category, amount in sorted(totals.items(), key=lambda item: -item[1]):
    print(f"{category} {amount:,}원")
