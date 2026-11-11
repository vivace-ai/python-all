message = "주문번호 A-1001, 상태: 배송준비"
print(message.replace("배송준비", "배송중"))

phone = "010-1234-5678"
print(phone.replace("-", ""))       # 빈 문자열로 바꾸면 지워진다
print(phone.replace("-", " ", 1))   # 세 번째 인자: 바꿀 횟수
