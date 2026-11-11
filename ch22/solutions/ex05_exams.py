from pathlib import Path

import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
path = Path(__file__).parent.parent / "data" / "study_log.csv"
df = pd.read_csv(path)

exams = df.dropna(subset=["score"])
result = exams.groupby("subject")["score"].agg(["count", "mean", "max"])
print(result.round(1))
