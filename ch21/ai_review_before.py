# AI가 내놓은 코드: 도시의 기온을 가져와 출력한다
import requests

BASE = "http://127.0.0.1:8021"


def get_temp(city):
    response = requests.get(f"{BASE}/weather", params={"city": city})
    return response.json().get("temp", 0)


for city in ["서울", "화성"]:
    print(f"{city}의 기온: {get_temp(city)}도")
