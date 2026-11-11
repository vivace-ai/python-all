scores = [72, 95, 48, 61, 88]

passed = [s for s in scores if s >= 60]     # 두 번 쓸 값은 리스트로 만든다
print("합격자 수:", len(passed))
print("합격 점수:", passed)
