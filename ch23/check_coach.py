# 모델을 부르지 않고 Coach가 무엇을 보내는지 확인한다
from study_log.coach import SYSTEM, Coach
from study_log.log import StudyLog
from study_log.storage import MemoryStorage

sent: list[list[dict]] = []


def fake_ask(messages: list[dict]) -> str:
    sent.append(messages)   # 받은 메시지를 기억해 둔다
    return "가짜 조언"


log = StudyLog(MemoryStorage())
log.add("파이썬", 1.5)
log.add("통계학", 1.0, score=85)

assert Coach(fake_ask).advise(log) == "가짜 조언"
assert sent[0][0] == {"role": "system", "content": SYSTEM}
assert "파이썬 1.5시간" in sent[0][1]["content"]
assert "평균 85.0점" in sent[0][1]["content"]
print("모든 확인을 통과했습니다.")
