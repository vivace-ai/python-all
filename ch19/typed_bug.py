def average(values: list[float]) -> float | None:
    """평균을 돌려준다. 값이 없으면 None."""
    if not values:
        return None
    return sum(values) / len(values)


scores = [72.0, 85.5]
result = average(scores)
print(result + 5)           # result는 None일 수도 있다
print(average("72, 85"))    # 리스트가 아니라 문자열을 넘겼다
