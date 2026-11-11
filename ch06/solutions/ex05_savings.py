monthly = 300_000   # 매달 넣는 돈
goal = 10_000_000   # 목표 금액

balance = 0
months = 0
while balance < goal:
    balance += monthly
    months += 1

print(f"{months}개월 뒤 {balance:,}원")
print(f"{months // 12}년 {months % 12}개월")
