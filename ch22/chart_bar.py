from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from kfont import use_korean_font

BASE = Path(__file__).parent
use_korean_font()

df = pd.read_csv(BASE / "data" / "study_log.csv")
totals = df.groupby("subject")["hours"].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(6, 3))      # 그림과 그래프 영역을 만든다
ax.bar(totals.index, totals.values, color="#1B2A4E", width=0.6)
ax.set_title("과목별 총 학습 시간")
ax.set_ylabel("시간")
for x, value in enumerate(totals.values):   # 막대 위에 값을 적는다
    ax.text(x, value + 0.3, f"{value:.1f}", ha="center")
ax.set_ylim(0, totals.max() + 2)
fig.tight_layout()

out = BASE / "output" / "by_subject.png"
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=200)                   # 파일로 저장한다
print(out.name, "저장")
