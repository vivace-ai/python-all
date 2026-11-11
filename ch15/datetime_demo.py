from datetime import date, timedelta

start = date(2026, 11, 2)
print(start, start.year, start.month)
print(start.strftime("%Y년 %m월 %d일"))     # 원하는 모양의 문자열로
print(start + timedelta(days=100))          # 100일 뒤
print((date(2026, 12, 31) - start).days)    # 두 날짜 사이의 일수
