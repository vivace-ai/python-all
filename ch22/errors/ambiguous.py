import pandas as pd

df = pd.DataFrame({"hours": [1.5, 2.0, 0.5]})

if df["hours"] > 1.0:
    print("긴 학습")
