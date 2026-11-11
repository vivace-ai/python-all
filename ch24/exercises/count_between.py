# 연습문제 3: AI가 작성한 함수. 독스트링과 동작이 다르다
def count_between(values: list[float], low: float, high: float) -> int:
    """low 이상 high 이하인 값의 수를 돌려준다."""
    return len([v for v in values if low < v < high])
