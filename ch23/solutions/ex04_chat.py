import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from llm import ask     # noqa: E402


class Chat:
    """대화 기록을 스스로 관리하는 대화 상대."""

    def __init__(self) -> None:
        self.history: list[dict] = []

    def say(self, text: str) -> str:
        self.history.append({"role": "user", "content": text})
        answer = ask(self.history)
        self.history.append({"role": "assistant", "content": answer})
        return answer


chat = Chat()
print(chat.say("내 이름은 준호야."))
print(chat.say("내 이름이 뭐라고 했지?"))
print(len(chat.history))
