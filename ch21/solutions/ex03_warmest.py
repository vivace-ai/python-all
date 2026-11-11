import requests

URL = "http://127.0.0.1:8021/weather"


def get_temp(city: str) -> float | None:
    """기온을 돌려준다. 서버가 모르는 도시면 None."""
    response = requests.get(URL, params={"city": city}, timeout=5)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()["temp"]


temps = {city: get_temp(city) for city in ["서울", "화성", "제주", "대구"]}
known = {city: temp for city, temp in temps.items() if temp is not None}
print("모르는 도시:", [city for city in temps if city not in known])
print("가장 따뜻한 곳:", max(known, key=known.get))
