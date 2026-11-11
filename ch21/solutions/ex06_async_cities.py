import asyncio

import httpx

BASE = "http://127.0.0.1:8021"


async def get_weather(client: httpx.AsyncClient, city: str) -> str:
    response = await client.get("/weather", params={"city": city})
    if response.status_code == 404:
        return f"{city}: 모르는 도시"
    data = response.json()
    return f"{city}: {data['temp']}도 {data['sky']}"


async def main() -> None:
    cities = ["서울", "화성", "부산", "제주"]
    async with httpx.AsyncClient(base_url=BASE, timeout=5) as client:
        lines = await asyncio.gather(*(get_weather(client, c) for c in cities))
    print("\n".join(lines))


asyncio.run(main())
