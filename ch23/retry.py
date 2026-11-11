import time

import requests

URL = "http://127.0.0.1:8023/v1/chat/completions"
AUTH = {"Authorization": "Bearer demo-key"}


def ask_with_retry(payload: dict, tries: int = 4) -> str:
    wait = 0.2
    for attempt in range(1, tries + 1):
        response = requests.post(URL, json=payload, headers=AUTH, timeout=30)
        if response.status_code != 429:
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        print(f"{attempt}번째 시도: 429. {wait}초 뒤에 다시 보낸다")
        time.sleep(wait)
        wait *= 2           # 기다리는 시간을 두 배로 늘린다
    raise RuntimeError(f"{tries}번 모두 거절당했다")


payload = {
    "model": "busy-model",  # 바쁜 척하는 연습용 모델
    "messages": [{"role": "user", "content": "변수가 뭐야?"}],
}
print(ask_with_retry(payload))
