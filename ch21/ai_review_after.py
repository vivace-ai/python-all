import requests

BASE = "http://127.0.0.1:8021"


def get_temp(city):
    """도시의 기온을 돌려준다. 가져오지 못하면 None."""
    response = requests.get(
        f"{BASE}/weather", params={"city": city}, timeout=5
    )
    if response.status_code == 404:
        return None                 # 없는 도시는 값이 없음을 알린다
    response.raise_for_status()     # 그 밖의 실패는 예외로 드러낸다
    return response.json()["temp"]  # 있어야 할 값은 대괄호로 꺼낸다


for city in ["서울", "화성"]:
    temp = get_temp(city)
    if temp is None:
        print(f"{city}의 기온을 찾을 수 없습니다.")
    else:
        print(f"{city}의 기온: {temp}도")
