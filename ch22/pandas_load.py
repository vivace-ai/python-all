from pathlib import Path

import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
path = Path(__file__).parent / "data" / "study_log.csv"
df = pd.read_csv(path)  # CSV 파일을 표로 읽는다

print(df.shape)         # (행의 수, 열의 수)
print(df.head())        # 앞의 다섯 행
print(df.dtypes)        # 열마다의 자료형
