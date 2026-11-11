def add_tax(price, rate=0.1):   # rate를 생략하면 0.1이 쓰인다
    return int(price * (1 + rate))


print(add_tax(10000))
print(add_tax(10000, 0.05))
print(add_tax(10000, rate=0))
