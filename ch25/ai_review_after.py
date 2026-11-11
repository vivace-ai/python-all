from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()
RECORDS = [{"day": 1, "subject": "파이썬", "hours": 1.5}]


@app.get("/records/{day}")
def get_record(day: int) -> dict:
    for record in RECORDS:
        if record["day"] == day:
            return record
    detail = f"{day}일차 기록이 없습니다."
    raise HTTPException(status_code=404, detail=detail)


client = TestClient(app)
for day in [1, 7]:
    response = client.get(f"/records/{day}")
    print(day, "->", response.status_code, response.json())
