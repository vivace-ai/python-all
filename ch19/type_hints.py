def format_hours(hours: float, unit: str = "시간") -> str:
    return f"{hours:.1f}{unit}"


def average(values: list[float]) -> float | None:
    """평균을 돌려준다. 값이 없으면 None."""
    if not values:
        return None
    return sum(values) / len(values)


count: int = 3  # 변수에도 붙일 수 있다
totals: dict[str, float] = {"파이썬": 3.5}

print(format_hours(1.5))
print(average([1.5, 2.0]), average([]))
print(format_hours.__annotations__)
