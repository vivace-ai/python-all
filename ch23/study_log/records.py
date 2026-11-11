"""기록 한 건을 나타내는 클래스들."""
from dataclasses import asdict, dataclass

from .errors import RecordError


@dataclass
class StudyRecord:
    """학습 기록 한 건."""

    day: int
    subject: str
    hours: float

    def __post_init__(self) -> None:
        if not 0 <= self.hours <= 24:
            raise RecordError(f"시간은 0에서 24 사이여야 한다: {self.hours}")

    def __str__(self) -> str:
        return f"{self.day}일차 {self.subject} {self.hours}시간"

    def to_line(self) -> str:
        """파일에 쓸 한 줄로 바꾼다."""
        return f"{self.day}\t{self.subject}\t{self.hours}\n"

    def to_dict(self) -> dict[str, object]:
        """JSON으로 내보낼 딕셔너리로 바꾼다. 자식의 속성도 함께 담긴다."""
        return asdict(self)


@dataclass
class ExamRecord(StudyRecord):
    """모의시험 기록. 학습 기록에 점수가 더해진다."""

    score: int = 0

    def __post_init__(self) -> None:
        super().__post_init__()
        if not 0 <= self.score <= 100:
            raise RecordError(f"점수는 0~100이어야 한다: {self.score}")

    def __str__(self) -> str:
        return f"{super().__str__()} [시험 {self.score}점]"

    def to_line(self) -> str:
        return super().to_line().rstrip("\n") + f"\t{self.score}\n"


def record_from_line(line: str) -> StudyRecord:
    """파일의 한 줄에서, 칸의 수에 맞는 종류의 기록을 만든다."""
    parts = line.strip().split("\t")
    try:
        if len(parts) == 3:
            day, subject, hours = parts
            return StudyRecord(int(day), subject, float(hours))
        if len(parts) == 4:
            day, subject, hours, score = parts
            return ExamRecord(int(day), subject, float(hours), int(score))
    except ValueError as e:
        raise RecordError(f"읽을 수 없는 줄이다: {line.strip()}") from e
    raise RecordError(f"칸의 수가 맞지 않는다: {line.strip()}")


def record_from_dict(data: dict) -> StudyRecord:
    """딕셔너리에서, 점수가 있고 없음에 맞는 종류의 기록을 만든다."""
    try:
        if data.get("score") is None:
            return StudyRecord(data["day"], data["subject"], data["hours"])
        return ExamRecord(data["day"], data["subject"], data["hours"],
                          data["score"])
    except (KeyError, TypeError) as e:
        raise RecordError(f"읽을 수 없는 기록이다: {data}") from e
