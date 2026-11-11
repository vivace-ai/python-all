import json

from llm import ask

question = "JSON으로 답해 줘: 파이썬을 한 시간 공부했다"
answer = ask([{"role": "user", "content": question}])
print(answer)
print(json.loads(answer))
