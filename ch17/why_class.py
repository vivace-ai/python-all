record = {"subject": "파이썬", "hours": 1.5}

record["hour"] = 2.0    # 키의 오타: 오류 없이 새 키가 생긴다
record["hours"] = -3    # 말이 안 되는 값도 그대로 들어간다
print(record)
