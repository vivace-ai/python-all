total = int(input("주문 금액: "))

if total >= 50000:
    shipping = 0
else:
    shipping = 3000

print(f"배송비: {shipping:,}원")
print(f"결제 금액: {total + shipping:,}원")
