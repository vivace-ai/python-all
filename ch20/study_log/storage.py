"""기록을 어디에 보관할지를 맡는다."""
from pathlib import Path
from typing import Protocol

from .errors import RecordError
from .records import StudyRecord, record_from_line


class Storage(Protocol):
    """기록을 읽어 오고 한 건씩 더할 수 있는 보관소."""

    def load(self) -> list[StudyRecord]: ...

    def append(self, record: StudyRecord) -> None: ...


class FileStorage:
    """탭으로 나눈 텍스트 파일에 보관한다."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> list[StudyRecord]:
        records: list[StudyRecord] = []
        try:
            with open(self.path, encoding="utf-8") as f:
                for line in f:
                    try:
                        records.append(record_from_line(line))
                    except RecordError:
                        continue    # 읽을 수 없는 줄은 건너뛴다
        except FileNotFoundError:
            pass                    # 첫 실행에는 파일이 없다
        return records

    def append(self, record: StudyRecord) -> None:
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(record.to_line())


class MemoryStorage:
    """메모리에만 보관한다. 파일 없이 시험할 때 쓴다."""

    def __init__(self) -> None:
        self.saved: list[StudyRecord] = []

    def load(self) -> list[StudyRecord]:
        return list(self.saved)

    def append(self, record: StudyRecord) -> None:
        self.saved.append(record)
