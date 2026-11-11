import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)
df = pd.DataFrame({
    "name": ["이서연", "박준호", "최민지", "정도윤"],
    "city": ["서울", "부산", "서울", "대구"],
    "age": [34, 41, 28, 37],
})

print(df.sort_values("age"))
print(df[df["city"] == "서울"]["name"].tolist())
print(df["age"].mean())
