import asyncio
import time


async def download(name: str, seconds: float) -> str:
    await asyncio.sleep(seconds)    # 내려받는 데 걸리는 시간을 흉내 낸다
    return f"{name} 완료"


async def main() -> None:
    files = [("보고서.pdf", 0.3), ("사진.zip", 0.5), ("메모.txt", 0.1)]
    start = time.perf_counter()
    results = await asyncio.gather(*(download(n, s) for n, s in files))
    print(results)
    print(f"{time.perf_counter() - start:.1f}초")


asyncio.run(main())
