import asyncio
import time

import httpx
import requests

BASE = "http://127.0.0.1:8021"
CITIES = ["서울", "부산", "대구", "제주"]


def fetch_one_by_one():
    """한 도시씩 차례로 요청한다."""
    temps = []
    for city in CITIES:
        params = {"city": city, "delay": 1}     # 응답에 1초가 걸리게 한다
        response = requests.get(f"{BASE}/weather", params=params, timeout=5)
        temps.append(response.json()["temp"])
    return temps


async def fetch_together():
    """네 도시를 한꺼번에 요청하고 함께 기다린다."""
    async with httpx.AsyncClient(base_url=BASE, timeout=5) as client:
        requests_ = [
            client.get("/weather", params={"city": city, "delay": 1})
            for city in CITIES
        ]
        responses = await asyncio.gather(*requests_)
    return [response.json()["temp"] for response in responses]


start = time.perf_counter()
print(fetch_one_by_one(), f"{time.perf_counter() - start:.1f}초")

start = time.perf_counter()
print(asyncio.run(fetch_together()), f"{time.perf_counter() - start:.1f}초")
