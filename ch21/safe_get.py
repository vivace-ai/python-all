import requests

BASE = "http://127.0.0.1:8021"
DEAD = "http://127.0.0.1:9"             # 아무도 듣고 있지 않은 주소


def get_weather(city, base=BASE, delay=0):
    """날씨를 딕셔너리로 돌려준다. 가져오지 못하면 까닭을 알리고 None."""
    params = {"city": city, "delay": delay}
    try:
        response = requests.get(f"{base}/weather", params=params, timeout=1)
        response.raise_for_status()     # 4xx, 5xx이면 예외를 일으킨다
    except requests.Timeout:
        print(f"{city}: 서버가 제때 답하지 않았습니다.")
    except requests.ConnectionError:
        print(f"{city}: 서버에 연결할 수 없습니다.")
    except requests.HTTPError as e:
        code = e.response.status_code
        print(f"{city}: 서버가 요청을 거절했습니다. ({code})")
    else:
        return response.json()
    return None


print(get_weather("서울"))
print(get_weather("화성"))              # 없는 도시
print(get_weather("부산", delay=2))     # 느린 응답
print(get_weather("제주", base=DEAD))   # 꺼진 서버
