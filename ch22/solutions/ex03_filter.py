from pathlib import Path

import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
path = Path(__file__).parent.parent / "data" / "study_log.csv"
df = pd.read_csv(path)

df["long"] = df["hours"] >= 2.0     # 참과 거짓으로 된 새 열
print(df["long"].sum(), "건")       # True는 1로 세어진다
print(df[df["long"]]["subject"].value_counts())
