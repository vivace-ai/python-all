hours = [2, 4, 1, 3, 5]     # 월~금 학습 시간
days = "월화수목금"

for day, hour in zip(days, hours):
    print(f"{day} {'■' * hour} {hour}시간")
