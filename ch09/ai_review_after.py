def add_item(item, items=None):
    if items is None:   # 넘겨받지 않았으면 호출할 때마다 새로 만든다
        items = []
    items.append(item)
    return items


cart_a = add_item("키보드")
cart_b = add_item("마우스")
print(cart_a)
print(cart_b)
