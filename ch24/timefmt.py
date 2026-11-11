def format_hours(hours: float) -> str:
    """시간을 읽기 좋은 글로 바꾼다. 1.5 -> '1시간 30분'"""
    total = round(hours * 60)
    h, m = divmod(total, 60)
    return f"{h}시간 {m}분"
