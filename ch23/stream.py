from llm import MODEL, client

question = [{"role": "user", "content": "파이썬을 한 문장으로 소개해 줘."}]
stream = client.chat.completions.create(
    model=MODEL, messages=question, stream=True
)

pieces = []
for chunk in stream:    # 조각이 도착할 때마다 한 바퀴 돈다
    piece = chunk.choices[0].delta.content or ""
    pieces.append(piece)
    print(piece, end="", flush=True)
print()
print(len(pieces), "조각으로 나뉘어 왔다")
