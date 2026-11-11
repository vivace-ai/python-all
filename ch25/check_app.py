# 서버도 모델도 켜지 않고 서비스 전체를 확인한다
import tempfile
from pathlib import Path

from fastapi.testclient import TestClient

import app as service

KEY = {"Authorization": "Bearer demo-key"}
sent: list[list[dict]] = []


def fake_ask(messages: list[dict]) -> str:
    sent.append(messages)
    return "가짜 조언"


with tempfile.TemporaryDirectory() as folder:
    service.DB_FILE = Path(folder) / "test.db"          # 빈 데이터베이스
    service.app.dependency_overrides[service.get_ask] = lambda: fake_ask
    client = TestClient(service.app)

    assert client.get("/records").json() == []
    assert client.get("/advice").status_code == 401     # 키가 없다
    response = client.get("/advice", headers=KEY)
    assert response.status_code == 404                  # 기록이 없다

    first = {"subject": "파이썬", "hours": 1.5}
    response = client.post("/records", json=first)
    assert response.status_code == 201
    assert response.json()["day"] == 1                  # 번호는 서버가 매긴다
    second = {"subject": "통계학", "hours": 1, "score": 85}
    client.post("/records", json=second)

    bad = client.post("/records", json={"subject": "영어", "hours": -3})
    assert bad.status_code == 422                       # 검증에 걸렸다
    assert len(client.get("/records").json()) == 2

    assert client.get("/summary").json() == {"파이썬": 1.5, "통계학": 1.0}
    response = client.get("/advice", headers=KEY)
    assert response.json() == {"advice": "가짜 조언"}
    assert "파이썬 1.5시간" in sent[0][1]["content"]

print("모든 확인을 통과했습니다.")
