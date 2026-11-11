# 학습 기록 프로그램 17단계: 기록을 LLM에 보여 주고 조언을 받는다
from pathlib import Path

from llm import ask
from study_log.coach import Coach, build_prompt
from study_log.log import StudyLog
from study_log.storage import FileStorage

DATA_FILE = Path(__file__).parent / "data" / "study_log.txt"

log = StudyLog(FileStorage(DATA_FILE))
print("[모델에 보낸 요약]")
print(build_prompt(log))
print()
print("[코치의 조언]")
print(Coach(ask).advise(log))
