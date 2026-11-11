import json

record = {
    "day": 1, "subject": "파이썬", "hours": 1.5,
    "tags": ["기초", "복습"], "score": None, "done": True,
}

text = json.dumps(record, ensure_ascii=False)   # 파이썬 값을 JSON 문자열로
print(text)
print(type(text).__name__)

back = json.loads(text)                         # JSON 문자열을 파이썬 값으로
print(back["tags"][0], back["score"], back == record)

print(json.dumps({"과목": "파이썬"}))           # ensure_ascii를 주지 않으면
