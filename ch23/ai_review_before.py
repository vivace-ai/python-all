# AI가 내놓은 코드: 메모를 모델에 보내 과목과 시간을 뽑아 기록한다
import json

from llm import ask

SYSTEM = (
    "문장에서 과목과 시간을 뽑아 JSON으로만 답한다. "
    '형식: {"subject": 문자열, "hours": 숫자}'
)
records = []

for memo in ["어제 파이썬을 한 시간 반 공부했다", "영어를 조금 공부했다"]:
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": memo},
    ]
    answer = ask(messages, response_format={"type": "json_object"})
    data = json.loads(answer)
    records.append(data)
    print(f"{data['subject']} {data['hours']}시간을 기록했습니다.")

print(records)
