import requests

BASE = "http://127.0.0.1:8021"

memo = {"text": "책 반납하기"}
created = requests.post(f"{BASE}/memos", json=memo, timeout=5)
created.raise_for_status()
saved = created.json()
print(created.status_code, saved["text"])

memos = requests.get(f"{BASE}/memos", timeout=5).json()
print(saved in memos)   # 방금 보낸 메모가 목록에 있다
