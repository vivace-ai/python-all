total = 0
for amount in [12000, -3000, 8500, 0, 23000]:
    if amount <= 0:     # 환불과 0원 항목은 집계하지 않는다
        continue
    total += amount
    print(f"{amount:>6}원 집계")

print(f"지출 합계: {total}원")
