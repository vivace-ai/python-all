n = int(input("N을 입력: "))

total = 0
for i in range(1, n + 1):
    total += i

print(f"1부터 {n}까지의 합: {total}")
print(f"공식 검산: {n * (n + 1) // 2}")
