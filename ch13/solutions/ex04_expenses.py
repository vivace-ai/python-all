from pathlib import Path

path = Path(__file__).parent.parent / "data" / "expenses.txt"

totals = {}
with open(path, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:    # 빈 줄은 건너뛴다
            continue
        category, amount = line.split(",")
        totals[category] = totals.get(category, 0) + int(amount)

for category in sorted(totals, key=totals.get, reverse=True):
    print(f"{category} {totals[category]:,}원")
print(f"합계 {sum(totals.values()):,}원")
