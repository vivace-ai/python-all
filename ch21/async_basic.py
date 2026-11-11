import asyncio
import time


async def brew(name, seconds):
    print(f"{name} 시작")
    await asyncio.sleep(seconds)    # 기다리는 동안 다른 일에 차례를 넘긴다
    print(f"{name} 완료")
    return f"{name} 한 잔"


async def main():
    start = time.perf_counter()
    # 셋을 함께 시작하고, 모두 끝날 때까지 기다린다
    results = await asyncio.gather(
        brew("커피", 0.3), brew("홍차", 0.2), brew("녹차", 0.1)
    )
    print(results)
    print(f"{time.perf_counter() - start:.1f}초")


asyncio.run(main())
