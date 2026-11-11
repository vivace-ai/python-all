scores = [72, 95, 48, 61, 88, 79]

top3 = sorted(scores, reverse=True)[:3]     # 큰 값부터 정렬해 앞의 셋
print(top3)
print(scores)                               # 원본의 순서는 그대로다
