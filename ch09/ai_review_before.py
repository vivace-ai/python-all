# AI가 내놓은 코드: 항목을 목록에 담아 돌려준다
def add_item(item, items=[]):
    items.append(item)
    return items


cart_a = add_item("키보드")
cart_b = add_item("마우스")     # 다른 고객의 장바구니
print(cart_a)
print(cart_b)
