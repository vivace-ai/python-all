def grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"                  # 어느 조건에도 맞지 않는 경우


for score in [95, 85, 75, 65]:  # 갈래마다 값을 하나씩 넣어 본다
    print(f"{score}점: {grade(score)}")
