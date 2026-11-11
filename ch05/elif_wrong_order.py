score = 95

if score >= 70:     # 95는 여기서 이미 참이다
    grade = "C"
elif score >= 80:
    grade = "B"
elif score >= 90:
    grade = "A"
else:
    grade = "F"

print(f"등급: {grade}")
