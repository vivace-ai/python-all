has_ticket = True
age = 17

if not has_ticket:  # 안 되는 경우부터 걸러 낸다
    print("표를 먼저 구매하세요.")
elif age < 19:
    print("성인만 입장할 수 있습니다.")
else:
    print("입장하세요.")
