NOTES = [
    "제너레이터는 값을 한꺼번에 만들지 않고 필요할 때 하나씩 내준다.",
    "딕셔너리는 키로 값을 찾는다. 키는 바뀌지 않는 자료형이어야 한다.",
    "with 문은 블록을 나갈 때 파일을 자동으로 닫아 준다.",
    "리스트는 모든 값을 메모리에 담아 두므로 여러 번 꺼내 쓸 수 있다.",
]


def pieces(text: str) -> set[str]:
    """글을 두 글자씩 잘라 조각의 집합으로 만든다."""
    return {text[i:i + 2] for i in range(len(text) - 1)}


def search(question: str, notes: list[str], count: int = 2) -> list[str]:
    """질문과 겹치는 조각이 많은 노트를 count개 고른다."""
    asked = pieces(question)

    def overlap(note: str) -> int:
        return len(asked & pieces(note))

    return sorted(notes, key=overlap, reverse=True)[:count]


question = "제너레이터는 리스트와 무엇이 다른가?"
found = search(question, NOTES)

prompt = "아래 노트만 근거로 답한다. 노트에 없으면 모른다고 답한다.\n"
prompt += "\n".join(f"- {note}" for note in found)
prompt += f"\n질문: {question}"
print(prompt)
