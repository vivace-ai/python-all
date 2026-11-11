# AI가 내놓은 코드: 모의시험의 평균 점수를 구한다
from pathlib import Path

import pandas as pd

path = Path(__file__).parent / "data" / "study_log.csv"
df = pd.read_csv(path)

df = df.fillna(0)   # 빈 값을 0으로 채운다
print(f"평균 점수: {df['score'].mean():.1f}점")
