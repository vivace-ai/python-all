text = input("점수(공백으로 구분): ")

scores = []
for part in text.split():
    scores.append(int(part))    # 조각을 정수로 바꿔 담는다

average = sum(scores) / len(scores)
print(f"개수 {len(scores)}, 합계 {sum(scores)}, 평균 {average:.1f}")
print(f"최고 {max(scores)}, 최저 {min(scores)}")
