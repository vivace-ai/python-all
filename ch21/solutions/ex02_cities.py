import requests

URL = "http://127.0.0.1:8021/weather"

for city in ["서울", "부산", "제주"]:
    response = requests.get(URL, params={"city": city}, timeout=5)
    response.raise_for_status()
    data = response.json()
    print(f"{data['city']} {data['temp']:>5.1f}도 {data['sky']}")
