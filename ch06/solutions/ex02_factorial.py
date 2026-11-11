n = int(input("N을 입력: "))

result = 1  # 곱의 누적은 1에서 출발한다
for i in range(1, n + 1):
    result *= i

print(f"{n}! = {result:,}")
