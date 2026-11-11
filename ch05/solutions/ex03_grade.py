score = int(input("점수: "))

if not 0 <= score <= 100:   # 범위 밖의 값부터 걸러 낸다
    print("0에서 100 사이의 점수를 입력하세요.")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    result = "합격" if score >= 60 else "불합격"
    print(f"등급 {grade}, {result}")
