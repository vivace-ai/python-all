# AI가 고쳐 준 코드: 분이 0이면 시간만 보이게 했다
def format_hours(hours: float) -> str:
    """시간을 읽기 좋은 글로 바꾼다. 1.5 -> '1시간 30분'"""
    h = int(hours)
    m = int((hours - h) * 60)
    if m == 0:
        return f"{h}시간"
    return f"{h}시간 {m}분"


for hours in [2.0, 1.5, 2.3]:
    print(hours, "->", format_hours(hours))
