import json
import tempfile
from pathlib import Path

from fastapi.testclient import TestClient

import app as service

with tempfile.TemporaryDirectory() as folder:
    service.DB_FILE = Path(folder) / "test.db"
    client = TestClient(service.app)
    response = client.post("/records", json={"subject": "영어", "hours": 30})

print(response.status_code)
for item in response.json()["detail"]:  # 어긋난 곳마다 한 항목
    print(json.dumps(item, ensure_ascii=False, indent=2))
