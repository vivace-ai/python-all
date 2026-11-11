import requests

BASE = "http://127.0.0.1:8021"              # 연습용 서버의 주소

params = {"city": "서울"}
response = requests.get(f"{BASE}/weather", params=params, timeout=5)

print(response.status_code)                 # 상태 코드
print(response.headers["Content-Type"])     # 응답의 형식
print(response.text)                        # 본문을 문자열 그대로
data = response.json()                      # 본문의 JSON을 파이썬 값으로
print(data["city"], data["temp"])
print(response.url)                         # 실제로 요청한 주소
