import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import tempfile                                     # noqa: E402
from contextlib import closing                      # noqa: E402

from fastapi.testclient import TestClient           # noqa: E402

import app as service                               # noqa: E402
from study_log.log import StudyLog                  # noqa: E402
from study_log.storage_sqlite import SqliteStorage  # noqa: E402


@service.app.get("/subjects")
def subjects() -> list[str]:
    """기록에 나온 과목을 가나다순으로 돌려준다."""
    with closing(SqliteStorage(service.DB_FILE)) as storage:
        return sorted(StudyLog(storage).total_by_subject())


with tempfile.TemporaryDirectory() as folder:
    service.DB_FILE = Path(folder) / "test.db"
    client = TestClient(service.app)
    assert client.get("/subjects").json() == []     # 먼저 적은 확인
    for subject in ["파이썬", "영어", "파이썬"]:
        client.post("/records", json={"subject": subject, "hours": 1})
    assert client.get("/subjects").json() == ["영어", "파이썬"]
    print(client.get("/subjects").json())

print("모든 확인을 통과했습니다.")
