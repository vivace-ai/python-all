import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from pydantic import ValidationError    # noqa: E402

from llm import ask                     # noqa: E402
from models import RecordIn             # noqa: E402

SYSTEM = (
    "문장에서 과목과 시간을 뽑아 JSON으로만 답한다. "
    '형식: {"subject": 문자열, "hours": 숫자}'
)


def extract(text: str) -> RecordIn | None:
    """모델의 답을 RecordIn으로 검증한다. 쓸 수 없으면 None."""
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": text},
    ]
    answer = ask(messages, response_format={"type": "json_object"})
    try:
        return RecordIn.model_validate_json(answer)
    except ValidationError:
        return None


for text in ["어제 파이썬을 한 시간 반 공부했다", "영어를 조금 공부했다"]:
    print(text, "->", extract(text))
