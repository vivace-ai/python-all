import json

from llm import ask

SYSTEM = (
    "문장에서 과목과 시간을 뽑아 JSON으로만 답한다. "
    '형식: {"subject": 문자열, "hours": 숫자}'
)


def to_record(data: object) -> dict:
    """모델의 답이 기록으로 쓸 수 있는 모양인지 검사한다."""
    if not isinstance(data, dict):
        raise ValueError("객체가 아니다")
    subject, hours = data.get("subject"), data.get("hours")
    if not isinstance(subject, str) or not subject:
        raise ValueError(f"과목이 없다: {subject}")
    if not isinstance(hours, (int, float)) or not 0 < hours <= 24:
        raise ValueError(f"시간이 숫자가 아니거나 범위를 벗어났다: {hours}")
    return {"subject": subject, "hours": float(hours)}


records = []
for memo in ["어제 파이썬을 한 시간 반 공부했다", "영어를 조금 공부했다"]:
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": memo},
    ]
    answer = ask(messages, response_format={"type": "json_object"})
    try:
        record = to_record(json.loads(answer))
    except ValueError as e:     # JSONDecodeError도 ValueError의 자식이다
        print(f"기록하지 못했습니다: {memo} ({e})")
        continue
    records.append(record)
    print(f"{record['subject']} {record['hours']}시간을 기록했습니다.")

print(records)
