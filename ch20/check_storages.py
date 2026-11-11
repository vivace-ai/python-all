# 보관소가 달라도 StudyLog가 똑같이 동작하는지 확인한다
from pathlib import Path

from study_log.log import StudyLog
from study_log.storage import FileStorage, MemoryStorage, Storage
from study_log.storage_json import JsonStorage
from study_log.storage_sqlite import SqliteStorage

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
for name in ("check.txt", "check.json", "check.db"):
    (OUT / name).unlink(missing_ok=True)    # 앞의 실행이 남긴 파일을 지운다

storages: list[Storage] = [
    MemoryStorage(),
    FileStorage(OUT / "check.txt"),
    JsonStorage(OUT / "check.json"),
    SqliteStorage(OUT / "check.db"),
]

for storage in storages:
    log = StudyLog(storage)
    log.add("파이썬", 1.5)
    log.add("통계학", 1.0, score=85)
    log.add("파이썬", 2.0)

    reloaded = StudyLog(storage)            # 같은 보관소에서 다시 불러온다
    assert len(reloaded) == 3
    assert reloaded.total_by_subject() == {"파이썬": 3.5, "통계학": 1.0}
    assert [exam.score for exam in reloaded.exams()] == [85]
    print(f"{type(storage).__name__:<14} 통과")
