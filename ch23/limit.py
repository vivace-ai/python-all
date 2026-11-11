import asyncio

from openai import AsyncOpenAI

from llm import API_KEY, BASE_URL, MODEL

client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)
limit = asyncio.Semaphore(2)    # 동시에 두 요청까지만 허락한다


async def ask(number: int) -> str:
    async with limit:           # 자리가 날 때까지 여기서 기다린다
        print(f"{number}번 요청을 보낸다")
        response = await client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "변수가 뭐야?"}],
        )
    return response.choices[0].message.content or ""


async def main() -> None:
    answers = await asyncio.gather(*(ask(n) for n in range(1, 5)))
    print(len(answers), "개의 답을 받았다")


asyncio.run(main())
