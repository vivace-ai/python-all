def to_korean_date(text):
    year, month, day = text.split("-")
    return f"{year}년 {int(month)}월 {int(day)}일"    # int()로 앞의 0을 없앤다


print(to_korean_date("2026-11-20"))
print(to_korean_date("2027-03-05"))
