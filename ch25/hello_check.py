from fastapi.testclient import TestClient

from hello import app

client = TestClient(app)    # 서버를 켜지 않고 요청을 보내는 도구

for url in ["/hello", "/hello?name=서연", "/double?n=21"]:
    response = client.get(url)
    print(url, "->", response.status_code, response.json())

response = client.get("/double?n=스물")
print(response.status_code, response.json()["detail"][0]["msg"])
