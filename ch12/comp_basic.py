prices = [12000, 8500, 23000]

# 9장의 방식: 빈 리스트를 만들고 하나씩 붙인다
with_tax = []
for price in prices:
    with_tax.append(price + price // 10)
print(with_tax)

# 같은 일을 한 줄로 쓴다
with_tax = [price + price // 10 for price in prices]
print(with_tax)
