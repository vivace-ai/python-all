import os

import requests

BASE = "http://127.0.0.1:8021"

# POST: 본문에 JSON을 실어 보낸다
memo = {"text": "우유 사기"}
response = requests.post(f"{BASE}/memos", json=memo, timeout=5)
print(response.status_code, response.json())

# 헤더 없이 요청하면 거절된다
response = requests.get(f"{BASE}/private", timeout=5)
print(response.status_code, response.json())

# API 키는 코드에 적지 않고 환경 변수에서 읽는다
api_key = os.environ.get("STUDY_API_KEY", "demo-key")
headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get(f"{BASE}/private", headers=headers, timeout=5)
print(response.status_code, response.json())
