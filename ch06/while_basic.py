balance = 10_000_000            # 원금 1,000만 원
target = balance * 2            # 목표: 두 배
years = 0

while balance < target:
    balance = balance * 1.05    # 해마다 5%씩 불어난다
    years += 1

print(f"{years}년 뒤 {balance:,.0f}원")
