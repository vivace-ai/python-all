import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))
from count_between import count_between as before   # noqa: E402


def count_between(values: list[float], low: float, high: float) -> int:
    """low 이상 high 이하인 값의 수를 돌려준다."""
    return len([v for v in values if low <= v <= high])


scores = [60, 75, 90]
print("고치기 전:", before(scores, 60, 90))
print("고친 뒤:", count_between(scores, 60, 90))

assert count_between(scores, 60, 90) == 3           # 양 끝을 포함한다
assert count_between(scores, 61, 89) == 1
assert count_between([], 0, 100) == 0
print("모든 확인을 통과했습니다.")
