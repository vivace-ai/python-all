# 학습 기록 프로그램 16단계: 쌓인 기록을 분석하고 그래프로 그린다
from pathlib import Path

import pandas as pd

from kfont import use_korean_font
from study_log.analysis import save_chart, subject_summary, to_frame
from study_log.log import StudyLog
from study_log.storage import FileStorage

pd.set_option("display.unicode.east_asian_width", True)
BASE = Path(__file__).parent


def main() -> None:
    log = StudyLog(FileStorage(BASE / "data" / "study_log.txt"))
    frame = to_frame(log)
    print(f"기록 {len(frame)}건, 총 {frame['hours'].sum():.1f}시간")
    print(subject_summary(frame))

    use_korean_font()
    chart = BASE / "output" / "report.png"
    save_chart(frame, chart)
    print(f"그래프를 {chart.name}에 저장했습니다.")


if __name__ == "__main__":
    main()
