from pathlib import Path

import pandas as pd

path = Path(__file__).parent.parent / "data" / "study_log.csv"
df = pd.read_csv(path, parse_dates=["date"])

df["weekday"] = df["date"].dt.day_of_week   # 월요일이 0, 일요일이 6
by_day = df.groupby("weekday")["hours"].sum()
names = ["월", "화", "수", "목", "금", "토", "일"]
for number, hours in by_day.items():
    print(names[number], hours)
print("가장 많이 공부한 요일:", names[by_day.idxmax()])
