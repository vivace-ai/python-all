def check_hours(hours):
    """학습 시간으로 쓸 수 있는 값인지 확인하고 그대로 돌려준다."""
    if not 0 <= hours <= 24:
        raise ValueError(f"시간은 0에서 24 사이여야 한다: {hours}")
    return hours


print(check_hours(2.5))

try:
    check_hours(30)
except ValueError as e:
    print("거절:", e)
