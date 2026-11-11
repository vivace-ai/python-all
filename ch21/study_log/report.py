"""기록을 표로 만드는 일을 맡는다."""
from tabulate import tabulate

from .log import StudyLog


def summary_table(log: StudyLog) -> str:
    """과목별 합계를 시간이 많은 순서의 표로 만든다."""
    totals = log.total_by_subject()
    rows = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    return tabulate(rows, headers=["과목", "시간"], floatfmt=".1f")


def exam_summary(log: StudyLog) -> str:
    """모의시험의 횟수와 평균 점수를 한 줄로 만든다. 없으면 빈 문자열."""
    exams = log.exams()
    if not exams:
        return ""
    average = sum(exam.score for exam in exams) / len(exams)
    return f"모의시험 {len(exams)}회, 평균 {average:.1f}점"
