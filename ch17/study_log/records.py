"""기록 한 건을 나타내는 클래스."""
from dataclasses import dataclass


@dataclass
class StudyRecord:
    day: int
    subject: str
    hours: float

    def __post_init__(self):
        """객체가 만들어진 직후에 값을 검사한다."""
        if not 0 <= self.hours <= 24:
            raise ValueError(f"시간은 0에서 24 사이여야 한다: {self.hours}")

    def __str__(self):
        return f"{self.day}일차 {self.subject} {self.hours}시간"

    def to_line(self):
        """파일에 쓸 한 줄로 바꾼다."""
        return f"{self.day}\t{self.subject}\t{self.hours}\n"

    @classmethod
    def from_line(cls, line):
        """파일의 한 줄로 기록을 만든다. 형식이 틀리면 ValueError가 난다."""
        day, subject, hours = line.strip().split("\t")
        return cls(int(day), subject, float(hours))
