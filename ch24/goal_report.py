# 학습 기록 프로그램 18단계: 과목별 목표와 달성 정도를 보여 준다
from pathlib import Path

from study_log.goal import format_progress, progress
from study_log.log import StudyLog
from study_log.storage import FileStorage

DATA_FILE = Path(__file__).parent / "data" / "study_log.txt"
GOALS: dict[str, float] = {
    "파이썬": 20, "영어": 12, "통계학": 10, "글쓰기": 8,
}

log = StudyLog(FileStorage(DATA_FILE))
items = progress(log, GOALS)
print(format_progress(items))

behind = [item for item in items if item.remaining > 0]
for item in behind:
    print(f"{item.subject}: 목표까지 {item.remaining:.1f}시간 남았습니다.")
