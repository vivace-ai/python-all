from llm import ask

question = {"role": "user", "content": "변수가 뭐야?"}

print(ask([question]))

system = {
    "role": "system",
    "content": "초등학생에게 설명하듯 쉬운 말로 답한다.",
}
print(ask([system, question]))
