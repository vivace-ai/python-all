from shop.cart import subtotal, total

cart = [("노트", 2500, 4), ("펜", 1200, 5)]
print(f"상품 금액 {subtotal(cart):,}원")
print(f"결제 금액 {total(cart):,}원")

cart.append(("가방", 39000, 1))
print(f"상품 금액 {subtotal(cart):,}원")
print(f"결제 금액 {total(cart):,}원")
