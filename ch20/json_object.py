import json
from dataclasses import asdict, dataclass
from datetime import date


@dataclass
class Task:
    title: str
    due: date
    done: bool = False


task = Task("보고서 제출", date(2026, 11, 30))

data = asdict(task)                 # 객체를 딕셔너리로
data["due"] = task.due.isoformat()  # 날짜는 문자열로 바꿔 넣는다
text = json.dumps(data, ensure_ascii=False)
print(text)

loaded = json.loads(text)
# 문자열을 다시 날짜로 바꾼 뒤, 딕셔너리를 풀어 객체를 만든다
loaded["due"] = date.fromisoformat(loaded["due"])
restored = Task(**loaded)
print(restored)
print(restored == task)
