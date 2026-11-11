"""기록을 표로 바꿔 분석하고 그래프로 그린다."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from .log import StudyLog


def to_frame(log: StudyLog) -> pd.DataFrame:
    """기록을 표로 바꾼다. 시험이 아닌 기록의 score는 비어 있다."""
    rows = [record.to_dict() for record in log.records]
    return pd.DataFrame(rows, columns=["day", "subject", "hours", "score"])


def subject_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """과목별 총 시간, 기록 수, 시험 평균을 시간이 많은 순서로 돌려준다."""
    summary = frame.groupby("subject").agg(
        hours=("hours", "sum"),
        records=("hours", "count"),
        exam_mean=("score", "mean"),    # 빈 값은 빼고 평균을 낸다
    )
    return summary.sort_values("hours", ascending=False).round(1)


def save_chart(frame: pd.DataFrame, path: Path) -> None:
    """과목별 시간과 시험 점수의 흐름을 한 장의 그림으로 저장한다."""
    totals = frame.groupby("subject")["hours"].sum().sort_values()
    exams = frame.dropna(subset=["score"])

    fig, (left, right) = plt.subplots(1, 2, figsize=(7.2, 2.8))
    left.barh(totals.index, totals.values, color="#1B2A4E")
    left.set_title("과목별 학습 시간")
    left.set_xlabel("시간")

    colors = ["#0F766E", "#C97A12", "#1B2A4E", "#6B7380"]
    for color, (subject, group) in zip(colors, exams.groupby("subject")):
        right.plot(group["day"], group["score"], marker="o", color=color,
                   label=subject)
    right.set_title("모의시험 점수")
    right.set_xlabel("기록 번호")
    right.legend()

    fig.tight_layout()
    path.parent.mkdir(exist_ok=True)
    fig.savefig(path, dpi=200)
    plt.close(fig)
