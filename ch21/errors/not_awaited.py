import asyncio


async def fetch_temp():
    await asyncio.sleep(0.1)
    return {"temp": 12.5}


async def main():
    data = fetch_temp()     # await를 빠뜨렸다
    print(data["temp"])


asyncio.run(main())
