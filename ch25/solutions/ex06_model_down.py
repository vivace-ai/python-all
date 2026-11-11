import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import tempfile                             # noqa: E402

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

    key = {"Authorization": "Bearer demo-key"}
    response = client.get("/advice", headers=key)
    assert response.status_code == 502
    print(response.status_code, response.json())
    # 조언이 실패해도 기록은 그대로 읽을 수 있어야 한다
    assert len(client.get("/records").json()) == 1

print("모든 확인을 통과했습니다.")
