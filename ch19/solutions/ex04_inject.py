from datetime import date


def is_birthday_month(birthday: date, today: date) -> bool:
    return birthday.month == today.month


def greeting(name: str, birthday: date, today: date) -> str:
    if is_birthday_month(birthday, today):
        return f"{name} 님, 생일이 있는 달입니다. 쿠폰을 보내 드렸습니다."
    return f"{name} 님, 안녕하세요."


birthday = date(1990, 11, 20)
print(greeting("이서연", birthday, today=date(2026, 11, 2)))
print(greeting("이서연", birthday, today=date(2026, 12, 1)))
