from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from kfont import use_korean_font

BASE = Path(__file__).parent
use_korean_font()

df = pd.read_csv(BASE / "data" / "study_log.csv", parse_dates=["date"])
daily = df.groupby("date")["hours"].sum()   # 날짜별 합계
total = daily.cumsum()                      # 그날까지의 누적

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(total.index, total.values, color="#0F766E", marker="o", markersize=3,
        label="누적")
ax.bar(daily.index, daily.values, color="#C97A12", alpha=0.5,
       label="그날의 학습")
ax.set_title("누적 학습 시간")
ax.set_ylabel("시간")
ax.legend()
fig.autofmt_xdate()                         # 날짜 눈금을 기울여 겹치지 않게
fig.tight_layout()

out = BASE / "output" / "cumulative.png"
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=200)
print(out.name, "저장")
