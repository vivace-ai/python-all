def add_tax(price):
    tax = price // 10   # 부가세 10%
    return price + tax


total = add_tax(12000)  # 호출한 자리가 반환값으로 바뀐다
print(total)
print(add_tax(8500) + add_tax(23000))
