from pathlib import Path

import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
path = Path(__file__).parent / "data" / "study_log.csv"
df = pd.read_csv(path)

# 비어 있는 칸의 수와 값이 있는 칸의 수
print(df["score"].isna().sum(), df["score"].notna().sum())
print(round(df["score"].mean(), 1))     # 빈 값은 빼고 계산한다

exams = df.dropna(subset=["score"])     # score가 빈 행을 뺀다
print(exams[["date", "subject", "score"]])
