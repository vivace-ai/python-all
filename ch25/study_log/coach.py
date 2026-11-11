"""기록을 요약해 LLM에 보내고 조언을 받는다."""
from collections.abc import Callable

from .log import StudyLog

SYSTEM = (
    "당신은 학습 코치다. "
    "학습 기록의 요약을 보고 세 문장 이내로 조언한다."
)

# 메시지 목록을 받아 모델의 답을 돌려주는 함수
Ask = Callable[[list[dict]], str]


def build_prompt(log: StudyLog) -> str:
    """모델에 보낼 기록 요약을 만든다."""
    lines = [f"기록 {len(log)}건"]
    for subject, hours in log.total_by_subject().items():
        lines.append(f"{subject} {hours:.1f}시간")
    exams = log.exams()
    if exams:
        average = sum(exam.score for exam in exams) / len(exams)
        lines.append(f"모의시험 {len(exams)}회, 평균 {average:.1f}점")
    return "\n".join(lines)


class Coach:
    def __init__(self, ask: Ask) -> None:
        self.ask = ask  # 모델을 부르는 함수를 건네받는다

    def advise(self, log: StudyLog) -> str:
        messages = [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": build_prompt(log)},
        ]
        return self.ask(messages)
