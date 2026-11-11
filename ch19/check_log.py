# 파일을 건드리지 않고 StudyLog가 제대로 동작하는지 확인한다
from study_log.log import StudyLog
from study_log.storage import MemoryStorage

storage = MemoryStorage()
log = StudyLog(storage)

log.add("파이썬", 1.5)
log.add("통계학", 1.0, score=85)
log.add("파이썬", 2.0)

assert len(log) == 3
assert log.next_day == 4
assert log.total_by_subject() == {"파이썬": 3.5, "통계학": 1.0}
assert [exam.score for exam in log.exams()] == [85]
assert len(storage.saved) == 3  # 보관소에도 세 건이 들어갔다

print("모든 확인을 통과했습니다.")
