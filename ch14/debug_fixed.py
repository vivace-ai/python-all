def average_top3(scores):
    """가장 높은 점수 세 개의 평균을 돌려준다."""
    ranked = sorted(scores, reverse=True)   # 높은 점수가 앞에 오게 한다
    top = ranked[:3]
    return sum(top) / len(top)


print(f"{average_top3([70, 95, 80, 60, 88]):.1f}")
