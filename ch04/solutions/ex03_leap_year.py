year = int(input("연도: "))

is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f"{year}년은 윤년인가: {is_leap}")
