import json
from dataclasses import dataclass

from llm import ask

SYSTEM = (
    "사용자의 문장에서 공부한 과목과 시간을 뽑아 JSON으로만 답한다. "
    '형식: {"subject": 문자열, "hours": 숫자}'
)


@dataclass
class Memo:
    subject: str
    hours: float


def extract(text: str) -> Memo:
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": text},
    ]
    answer = ask(messages, response_format={"type": "json_object"})
    data = json.loads(answer)   # 문자열을 딕셔너리로
    return Memo(data["subject"], float(data["hours"]))


print(extract("어제 파이썬을 한 시간 반 공부했다"))
print(extract("통계학 책을 두 시간 읽었다"))
