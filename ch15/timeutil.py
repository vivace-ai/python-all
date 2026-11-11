"""학습 시간을 다루는 도우미 함수 모음."""

MINUTES_PER_HOUR = 60


def to_minutes(hours):
    """시간을 분으로 바꾼다."""
    return round(hours * MINUTES_PER_HOUR)


def format_hours(hours):
    """1.5를 '1시간 30분'으로 바꾼다."""
    minutes = to_minutes(hours)
    h = minutes // MINUTES_PER_HOUR
    m = minutes % MINUTES_PER_HOUR
    return f"{h}시간 {m}분" if m else f"{h}시간"


if __name__ == "__main__":
    # 이 파일을 직접 실행할 때만 실행된다
    print(format_hours(1.5))
    print(format_hours(2))
