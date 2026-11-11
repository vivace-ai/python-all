import re


def to_korean(m):
    year, month, day = m.groups()
    return f"{year}년 {int(month)}월 {int(day)}일"  # int()가 앞의 0을 뗀다


text = "접수는 2026-11-02부터 2026-12-05까지입니다."
print(re.sub(r"(\d{4})-(\d{2})-(\d{2})", to_korean, text))
