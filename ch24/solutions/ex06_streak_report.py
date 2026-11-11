import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from streak import longest_streak                           # noqa: E402
from study_log.log import StudyLog                          # noqa: E402
from study_log.storage import FileStorage, MemoryStorage    # noqa: E402


def study_streak(log: StudyLog) -> int:
    """기록에서 가장 길게 이어진 학습 일수를 구한다."""
    return longest_streak([record.day for record in log.records])


# 먼저 적은 확인
empty = StudyLog(MemoryStorage())
assert study_streak(empty) == 0
empty.add("파이썬", 1.0)
assert study_streak(empty) == 1

data_file = Path(__file__).parent.parent / "data" / "study_log.txt"
log = StudyLog(FileStorage(data_file))
print(f"기록 {len(log)}건, 가장 길게 이어진 학습: {study_streak(log)}일")
