"""기록을 JSON 파일 하나에 보관한다."""
import json
from pathlib import Path

from .records import StudyRecord, record_from_dict


class JsonStorage:
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> list[StudyRecord]:
        try:
            with open(self.path, encoding="utf-8") as f:
                return [record_from_dict(item) for item in json.load(f)]
        except FileNotFoundError:
            return []

    def append(self, record: StudyRecord) -> None:
        # JSON은 끝에 덧붙일 수 없다. 전체를 읽어 한 건을 더한 뒤 다시 쓴다
        items = [r.to_dict() for r in self.load()] + [record.to_dict()]
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
