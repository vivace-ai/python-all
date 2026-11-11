"""기록 전체를 맡는 클래스."""
from collections import Counter

from .errors import RecordError
from .records import ExamRecord, StudyRecord, record_from_line


class StudyLog:
    """파일 하나에 저장되는 학습 기록 모음."""

    def __init__(self, path):
        self.path = path
        self.records = []
        self.skipped = 0    # 읽지 못하고 건너뛴 줄의 수
        self._load()

    def _load(self):
        try:
            with open(self.path, encoding="utf-8") as f:
                for line in f:
                    try:
                        self.records.append(record_from_line(line))
                    except RecordError:
                        self.skipped += 1
        except FileNotFoundError:
            pass            # 첫 실행에는 파일이 없다. 빈 기록으로 시작한다

    def __len__(self):
        return len(self.records)

    @property
    def next_day(self):
        """다음 기록에 붙일 일차 번호."""
        return self.records[-1].day + 1 if self.records else 1

    def add(self, subject, hours, score=None):
        """기록을 만들어 파일에 덧붙이고, 만든 기록을 돌려준다."""
        if score is None:
            record = StudyRecord(self.next_day, subject, hours)
        else:
            record = ExamRecord(self.next_day, subject, hours, score)
        with open(self.path, "a", encoding="utf-8") as f:
            # 기록의 종류에 맞는 to_line()이 불린다
            f.write(record.to_line())
        self.records.append(record)
        return record

    def total_by_subject(self):
        """과목별 총 학습 시간을 돌려준다."""
        totals = Counter()
        for record in self.records:
            totals[record.subject] += record.hours
        return totals

    def exams(self):
        """모의시험 기록만 골라 돌려준다."""
        return [r for r in self.records if isinstance(r, ExamRecord)]
