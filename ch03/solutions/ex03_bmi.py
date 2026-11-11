height = float(input("키(cm): "))
weight = float(input("몸무게(kg): "))

meter = height / 100
bmi = weight / (meter * meter)  # BMI = 몸무게(kg) / 키(m)의 제곱

print(f"BMI: {bmi:.1f}")
