is_member = True
coupon = ""

if is_member:   # is_member == True 라고 쓰지 않는다
    print("회원 가격을 적용합니다.")

if not coupon:  # 빈 문자열은 거짓으로 친다
    print("적용할 쿠폰이 없습니다.")
