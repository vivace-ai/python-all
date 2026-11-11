from pydantic import ValidationError

from models import RecordIn

record = RecordIn(subject="파이썬", hours="1.5")    # 문자열 "1.5"를 넘겼다
print(record)
print(record.model_dump())

# JSON 문자열에서 곧바로 만든다. 23장의 '조금'을 다시 넣어 본다
try:
    RecordIn.model_validate_json('{"subject": "영어", "hours": "조금"}')
except ValidationError as e:
    print("거절:", e.errors()[0]["loc"], e.errors()[0]["msg"])
