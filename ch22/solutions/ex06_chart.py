import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).parent.parent
sys.path.insert(0, str(BASE))       # 한 단계 위의 kfont.py를 가져오려고
from kfont import use_korean_font   # noqa: E402

use_korean_font()
df = pd.read_csv(BASE / "data" / "study_log.csv")
counts = df["subject"].value_counts()

fig, ax = plt.subplots(figsize=(5, 3))
ax.barh(counts.index, counts.values, color="#0F766E")
ax.set_title("과목별 기록 횟수")
ax.set_xlabel("횟수")
fig.tight_layout()

out = BASE / "output" / "counts.png"
out.parent.mkdir(exist_ok=True)
fig.savefig(out, dpi=200)
print(counts.to_dict())
print(out.name, "저장")
