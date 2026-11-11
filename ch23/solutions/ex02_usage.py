import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from llm import MODEL, client       # noqa: E402

PRICE_IN, PRICE_OUT = 3.0, 15.0     # 100만 토큰당 달러. 예로 든 값이다

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "파이썬을 한 문장으로 소개해 줘."},
    ],
)
usage = response.usage
cost = usage.prompt_tokens * PRICE_IN + usage.completion_tokens * PRICE_OUT
cost /= 1_000_000
print(f"입력 {usage.prompt_tokens}토큰, 출력 {usage.completion_tokens}토큰")
print(f"이 요청의 비용: {cost:.6f}달러")
print(f"하루 1만 번이면: {cost * 10_000:.2f}달러")
