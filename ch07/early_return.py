def shipping_fee(total):
    if total < 0:
        return None     # 잘못된 값은 여기서 끝낸다
    if total >= 50000:
        return 0
    return 3000         # 위의 어느 경우도 아닐 때


print(shipping_fee(62000), shipping_fee(30000), shipping_fee(-1))
