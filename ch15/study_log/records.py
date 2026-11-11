"""기록 한 건의 모양과 검사를 맡는다."""


def check_hours(hours):
    """학습 시간으로 쓸 수 있는 값인지 확인하고 그대로 돌려준다."""
    if not 0 <= hours <= 24:
        raise ValueError(f"시간은 0에서 24 사이여야 한다: {hours}")
    return hours


def make_record(day, subject, hours_text):
    """문자열로 받은 값을 검사해 기록 하나를 만든다."""
    hours = check_hours(float(hours_text))
    return {"day": int(day), "subject": subject, "hours": hours}
