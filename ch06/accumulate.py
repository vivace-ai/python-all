sales = [120, 95, 143, 110]     # 1~4분기 매출(만 원)
total = 0                       # 누적할 변수는 0에서 출발한다
for amount in sales:
    total += amount             # total = total + amount
    print(f"{amount:>4} 더함 -> 합계 {total:>4}")
print(f"연간 매출: {total}만 원")
