def longest_streak(days: list[int]) -> int:
    """가장 길게 이어진 학습 일수를 돌려준다."""
    if not days:
        return 0
    days = sorted(set(days))    # 같은 날의 기록은 하루로 친다
    best = run = 1
    for prev, cur in zip(days, days[1:]):
        if cur == prev + 1:
            run += 1
            best = max(best, run)
        else:
            run = 1
    return best
