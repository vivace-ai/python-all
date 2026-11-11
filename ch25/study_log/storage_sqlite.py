"""기록을 SQLite 데이터베이스에 보관한다."""
import sqlite3
from pathlib import Path

from .records import StudyRecord, record_from_dict

CREATE = """
    CREATE TABLE IF NOT EXISTS records (
        day     INTEGER NOT NULL,
        subject TEXT    NOT NULL,
        hours   REAL    NOT NULL,
        score   INTEGER
    )
"""


class SqliteStorage:
    def __init__(self, path: Path | str) -> None:
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute(CREATE)

    def load(self) -> list[StudyRecord]:
        rows = self.conn.execute(
            "SELECT day, subject, hours, score FROM records ORDER BY day"
        )
        return [record_from_dict(dict(row)) for row in rows]

    def append(self, record: StudyRecord) -> None:
        data = record.to_dict()
        with self.conn:     # 블록이 끝나면 commit, 예외가 나면 되돌린다
            self.conn.execute(
                "INSERT INTO records (day, subject, hours, score)"
                " VALUES (?, ?, ?, ?)",
                (data["day"], data["subject"], data["hours"],
                 data.get("score")),
            )

    def close(self) -> None:
        """데이터베이스 연결을 닫는다."""
        self.conn.close()
