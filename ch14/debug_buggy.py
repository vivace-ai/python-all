def average_top3(scores):
    """가장 높은 점수 세 개의 평균을 돌려준다."""
    ranked = sorted(scores)
    top = ranked[:3]
    return sum(top) / 3


print(average_top3([70, 95, 80, 60, 88]))
