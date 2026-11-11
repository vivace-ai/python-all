"""기록 전체를 맡는 클래스."""
from .records import ExamRecord, StudyRecord
from .storage import Storage


class StudyLog:
    """학습 기록 모음. 보관은 건네받은 보관소에 맡긴다."""

    def __init__(self, storage: Storage) -> None:
        self.storage = storage
        self.records: list[StudyRecord] = storage.load()

    def __len__(self) -> int:
        return len(self.records)

    @property
    def next_day(self) -> int:
        """다음 기록에 붙일 일차 번호."""
        return self.records[-1].day + 1 if self.records else 1

    def add(self, subject: str, hours: float,
            score: int | None = None) -> StudyRecord:
        """기록을 만들어 보관소에 더하고, 만든 기록을 돌려준다."""
        record: StudyRecord
        if score is None:
            record = StudyRecord(self.next_day, subject, hours)
        else:
            record = ExamRecord(self.next_day, subject, hours, score)
        self.storage.append(record)
        self.records.append(record)
        return record

    def total_by_subject(self) -> dict[str, float]:
        """과목별 총 학습 시간을 돌려준다."""
        totals: dict[str, float] = {}
        for record in self.records:
            subject = record.subject
            totals[subject] = totals.get(subject, 0) + record.hours
        return totals

    def exams(self) -> list[ExamRecord]:
        """모의시험 기록만 골라 돌려준다."""
        return [r for r in self.records if isinstance(r, ExamRecord)]
