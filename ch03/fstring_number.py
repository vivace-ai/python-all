pi = 3.141592653589793
amount = 1234567890
rate = 0.156

print(f"{pi:.2f}")      # 소수 둘째 자리까지
print(f"{pi:.4f}")      # 소수 넷째 자리까지
print(f"{amount:,}원")  # 천 단위 쉼표
print(f"{rate:.1%}")    # 백분율, 소수 첫째 자리까지
print(f"{7:03d}")       # 세 자리로 맞추고 빈 곳은 0
