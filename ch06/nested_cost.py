for n in [10, 100, 1000]:
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print(f"n = {n:>4} -> 안쪽 본문 실행 {count:>9,}회")
