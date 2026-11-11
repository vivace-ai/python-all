age = int(input("나이: "))
is_member = input("회원입니까 (y/n): ") == "y"
total = int(input("주문 금액: "))

by_age = age < 8 or age >= 65               # 미취학 아동 또는 경로 우대
by_order = is_member and total >= 30000     # 회원이면서 3만 원 이상

print(f"할인 대상: {by_age or by_order}")
