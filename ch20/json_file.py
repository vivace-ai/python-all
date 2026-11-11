import json
from pathlib import Path

path = Path(__file__).parent / "output" / "records.json"
path.parent.mkdir(exist_ok=True)

records = [
    {"day": 1, "subject": "파이썬", "hours": 1.5},
    {"day": 2, "subject": "통계학", "hours": 1.0},
]
with open(path, "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)     # 파일에 쓴다

print(path.read_text(encoding="utf-8"))

with open(path, encoding="utf-8") as f:
    loaded = json.load(f)                                   # 파일에서 읽는다
print(sum(record["hours"] for record in loaded))
