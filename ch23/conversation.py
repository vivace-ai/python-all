from llm import ask

# 요청을 따로 보내면 모델은 앞의 요청을 모른다
print(ask([{"role": "user", "content": "내 이름은 서연이야."}]))
print(ask([{"role": "user", "content": "내 이름이 뭐라고 했지?"}]))

# 대화를 이으려면 지금까지의 메시지를 모두 다시 보낸다
history = []
for text in ["내 이름은 서연이야.", "내 이름이 뭐라고 했지?"]:
    history.append({"role": "user", "content": text})
    answer = ask(history)
    history.append({"role": "assistant", "content": answer})
    print(answer)

print(len(history), "개의 메시지가 쌓였다")
