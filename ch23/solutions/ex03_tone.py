import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from llm import ask     # noqa: E402


def explain(question: str, audience: str | None = None) -> str:
    """질문을 보낸다. audience를 주면 그 사람에게 설명하듯 답하게 한다."""
    messages = []
    if audience:
        content = f"{audience}에게 설명하듯 쉬운 말로 답한다."
        messages.append({"role": "system", "content": content})
    messages.append({"role": "user", "content": question})
    return ask(messages)


print(explain("변수가 뭐야?"))
print(explain("변수가 뭐야?", audience="초등학생"))
