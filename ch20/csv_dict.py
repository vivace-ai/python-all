import csv
from pathlib import Path

path = Path(__file__).parent / "output" / "members.csv"
path.parent.mkdir(exist_ok=True)

members = [
    {"name": "이서연", "city": "서울", "age": 34},
    {"name": "박준호", "city": "부산", "age": 41},
]
with open(path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "city", "age"])
    writer.writeheader()                # 첫 줄에 열 이름을 쓴다
    writer.writerows(members)

with open(path, encoding="utf-8", newline="") as f:
    loaded = list(csv.DictReader(f))    # 첫 줄을 키로 삼아 딕셔너리로 읽는다

print(loaded[0])
print(sum(int(member["age"]) for member in loaded) / len(loaded))
