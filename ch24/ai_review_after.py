def format_hours(hours: float) -> str:
    """시간을 읽기 좋은 글로 바꾼다. 1.5 -> '1시간 30분'"""
    total = round(hours * 60)
    h, m = divmod(total, 60)
    if m == 0:                              # 더한 것은 이 두 줄뿐이다
        return f"{h}시간"
    return f"{h}시간 {m}분"


assert format_hours(1.5) == "1시간 30분"    # 전부터 있던 확인
assert format_hours(2.3) == "2시간 18분"
assert format_hours(0.25) == "0시간 15분"
assert format_hours(2.0) == "2시간"         # 이번에 더한 확인
for hours in [2.0, 1.5, 2.3]:
    print(hours, "->", format_hours(hours))
