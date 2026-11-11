total = int(input("주문 금액: "))

if total >= 50000:  # '이상'은 그 값을 포함한다
    shipping = 0
else:
    shipping = 3000

print(f"배송비: {shipping:,}원")
