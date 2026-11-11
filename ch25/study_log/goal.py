"""과목별 목표 시간과 달성 정도."""
from dataclasses import dataclass

from .log import StudyLog


@dataclass
class Progress:
    """한 과목의 목표와 지금까지 공부한 시간."""

    subject: str
    done: float
    goal: float

    @property
    def percent(self) -> int:
        """달성률. 100을 넘지 않는다."""
        return min(100, round(self.done / self.goal * 100))

    @property
    def remaining(self) -> float:
        """목표까지 남은 시간."""
        return max(0, self.goal - self.done)


def progress(log: StudyLog, goals: dict[str, float]) -> list[Progress]:
    """목표가 있는 과목마다 달성 정도를 구한다."""
    for subject, goal in goals.items():
        if goal <= 0:
            raise ValueError(f"목표는 0보다 커야 한다: {subject} {goal}")
    totals = log.total_by_subject()
    return [Progress(s, totals.get(s, 0), g) for s, g in goals.items()]


def format_progress(items: list[Progress]) -> str:
    """달성 정도를 막대와 함께 여러 줄의 글로 만든다."""
    lines = []
    for item in items:
        filled = item.percent // 10
        bar = "#" * filled + "." * (10 - filled)
        lines.append(
            f"[{bar}] {item.percent:>3}%  {item.subject} "
            f"{item.done:.1f}/{item.goal:.1f}시간"
        )
    return "\n".join(lines)
