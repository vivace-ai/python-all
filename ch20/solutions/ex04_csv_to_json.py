import csv
import json
from pathlib import Path

BASE = Path(__file__).parent.parent
source = BASE / "data" / "sales.csv"
target = BASE / "output" / "sales.json"
target.parent.mkdir(exist_ok=True)

with open(source, encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:    # CSV에서 읽은 값은 모두 문자열이다
    row["price"] = int(row["price"])
    row["count"] = int(row["count"])

with open(target, "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)
print(len(rows), "건을", target.name, "에 저장했습니다.")
print(json.dumps(rows[1], ensure_ascii=False))
