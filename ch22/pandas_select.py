from pathlib import Path

import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
path = Path(__file__).parent / "data" / "study_log.csv"
df = pd.read_csv(path)

print(df["hours"].sum(), df["hours"].mean())    # 열 하나를 꺼내 계산한다

long_days = df[df["hours"] >= 2.5]              # 조건에 맞는 행만 고른다
print(long_days)

# 조건이 둘이면 괄호로 감싸고 &로 잇는다
python = df[(df["subject"] == "파이썬") & (df["hours"] >= 2.0)]
print(python[["date", "hours"]])

df["minutes"] = df["hours"] * 60                # 새 열을 만든다
print(df.sort_values("hours", ascending=False).head(3))
