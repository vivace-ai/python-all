# AI가 내놓은 코드: 점수를 등급으로 바꾸는 함수
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"


print("95점:", grade(95))
print("65점:", grade(65))
