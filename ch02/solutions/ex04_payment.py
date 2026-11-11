unit_price = 18000
quantity = 4
discount_rate = 0.15

subtotal = unit_price * quantity
discount = int(subtotal * discount_rate)    # 원 단위 아래는 버린다
payment = subtotal - discount

print("주문 금액:", subtotal, "원")
print("할인 금액:", discount, "원")
print("결제 금액:", payment, "원")
