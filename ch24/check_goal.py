# 목표 기능이 지켜야 할 것을 먼저 적는다
from study_log.goal import progress
from study_log.log import StudyLog
from study_log.storage import MemoryStorage

log = StudyLog(MemoryStorage())
log.add("파이썬", 3.0)
log.add("영어", 1.0)
log.add("파이썬", 4.5)

items = progress(log, {"파이썬": 10, "영어": 0.5, "통계학": 4})
assert [item.subject for item in items] == ["파이썬", "영어", "통계학"]
assert [item.done for item in items] == [7.5, 1.0, 0]
# 달성률은 100을 넘지 않는다
assert [item.percent for item in items] == [75, 100, 0]
assert [item.remaining for item in items] == [2.5, 0, 4]

try:
    progress(log, {"파이썬": 0})
except ValueError:
    pass
else:
    raise AssertionError("목표가 0이면 ValueError가 나야 한다")

print("모든 확인을 통과했습니다.")
