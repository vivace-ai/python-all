# AI가 내놓은 코드: 5만 원 이상이면 배송비가 무료다
total = int(input("주문 금액: "))

if total > 50000:
    shipping = 0
else:
    shipping = 3000

print(f"배송비: {shipping:,}원")
