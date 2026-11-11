# AI가 내놓은 코드: 일차 번호로 기록 한 건을 찾는다
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
RECORDS = [{"day": 1, "subject": "파이썬", "hours": 1.5}]


@app.get("/records/{day}")
def get_record(day: int) -> dict:
    for record in RECORDS:
        if record["day"] == day:
            return record
    return {"error": "기록이 없습니다."}


client = TestClient(app)
for day in [1, 7]:
    response = client.get(f"/records/{day}")
    print(day, "->", response.status_code, response.json())
