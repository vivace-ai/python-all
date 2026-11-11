scores = [72, 95, 48, 61, 88]

print(sum(scores), len(scores))
print(max(scores), min(scores))
print(sum(scores) / len(scores))    # 평균
print(scores.index(95))             # 값이 있는 위치

passed = []                         # 조건에 맞는 값만 모은다
for score in scores:
    if score >= 60:
        passed.append(score)
print(passed)
