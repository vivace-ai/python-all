import logging
import sys
import tempfile
from pathlib import Path

# 로그가 실행 결과에 보이도록 표준 출력으로 보낸다. 시각은 뺐다
logging.basicConfig(stream=sys.stdout, format="%(levelname)s %(message)s")

import httpx                                # noqa: E402
import openai                               # noqa: E402
from fastapi.testclient import TestClient   # noqa: E402

import app as service                       # noqa: E402


def broken_ask(messages: list[dict]) -> str:
    """모델 서비스가 멈춘 상황을 흉내 낸다."""
    request = httpx.Request("POST", "http://127.0.0.1:8023/v1")
    raise openai.APIConnectionError(request=request)


with tempfile.TemporaryDirectory() as folder:
    service.DB_FILE = Path(folder) / "test.db"
    service.app.dependency_overrides[service.get_ask] = lambda: broken_ask
    client = TestClient(service.app)
    client.post("/records", json={"subject": "파이썬", "hours": 1.5})
    client.post("/records", json={"subject": "영어", "hours": 1, "score": 90})
    client.get("/advice", headers={"Authorization": "Bearer demo-key"})
