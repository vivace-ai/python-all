# AI가 내놓은 코드: 합격자 수와 합격 점수를 출력한다
scores = [72, 95, 48, 61, 88]

passed = (s for s in scores if s >= 60)
print("합격자 수:", len(list(passed)))
print("합격 점수:", list(passed))
