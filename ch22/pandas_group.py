from pathlib import Path

import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
path = Path(__file__).parent / "data" / "study_log.csv"
df = pd.read_csv(path, parse_dates=["date"])    # date 열을 날짜로 읽는다

# 과목별로 묶어 합계, 평균, 건수를 구한다
summary = df.groupby("subject")["hours"].agg(["sum", "mean", "count"])
print(summary.sort_values("sum", ascending=False))

# 날짜에서 주 번호를 뽑아 주별로 묶는다
df["week"] = df["date"].dt.isocalendar().week
print(df.groupby("week")["hours"].sum())
