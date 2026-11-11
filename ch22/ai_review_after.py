from pathlib import Path

import pandas as pd

path = Path(__file__).parent / "data" / "study_log.csv"
df = pd.read_csv(path)

scores = df["score"].dropna()   # 시험을 본 날만 남긴다
print(f"전체 {len(df)}건 가운데 시험 {len(scores)}건")
print(f"평균 점수: {scores.mean():.1f}점")
