import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from llm import MODEL, client   # noqa: E402


def stream_answer(question: str):
    """답의 조각을 하나씩 내주는 제너레이터."""
    stream = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": question}],
        stream=True,
    )
    for chunk in stream:
        piece = chunk.choices[0].delta.content
        if piece:
            yield piece


words = 0
for piece in stream_answer("변수가 뭐야?"):
    words += 1
    print(piece, end="", flush=True)
print(f"\n{words}조각")
