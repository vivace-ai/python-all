import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from llm import ask     # noqa: E402

SYSTEM = (
    "문장에서 과목과 시간을 뽑아 JSON으로만 답한다. "
    '형식: {"subject": 문자열, "hours": 숫자}'
)


def extract(text: str) -> dict | None:
    """과목과 시간을 뽑는다. 쓸 수 없는 답이면 None."""
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": text},
    ]
    try:
        answer = ask(messages, response_format={"type": "json_object"})
        data = json.loads(answer)
        hours = float(data["hours"])
    except (ValueError, KeyError, TypeError):
        return None
    return {"subject": data["subject"], "hours": hours}


for text in ["글쓰기를 30분 했다", "통계학을 두 시간 공부했다", "영어를 조금 봤다"]:
    print(text, "->", extract(text))
