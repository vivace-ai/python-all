from datetime import date


def days_left_fixed(deadline):
    return (deadline - date.today()).days   # 오늘 날짜를 안에서 구한다


def days_left(deadline, today):
    return (deadline - today).days          # 오늘 날짜를 건네받는다


deadline = date(2026, 12, 31)
print(days_left(deadline, today=date(2026, 11, 2)))
print(days_left(deadline, today=date(2026, 12, 31)))
print(days_left(deadline, today=date(2027, 1, 2)))
