height = float(input("키(cm): "))
weight = float(input("몸무게(kg): "))

bmi = weight / (height / 100) ** 2

if bmi < 18.5:
    category = "저체중"
elif bmi < 23:
    category = "정상"
elif bmi < 25:
    category = "과체중"
else:
    category = "비만"

print(f"BMI {bmi:.1f}: {category}")
