budget = 50_000
spent = 0

for price in [12000, 8500, 23000, 15000, 4000]:
    if spent + price > budget:
        print(f"{price}원은 예산을 넘어 담지 않습니다.")
        break
    spent += price
    print(f"{price:>6}원 담음 (누계 {spent}원)")

print(f"결제 금액: {spent}원")
