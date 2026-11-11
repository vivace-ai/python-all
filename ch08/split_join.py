line = "키보드,89000,2"
name, price, quantity = line.split(",")     # 쉼표에서 끊어 나눈다
print(name, int(price) * int(quantity))

words = "파이썬은   읽기   쉽다".split()    # 공백에서 끊는다
print(words)

print("/".join(["2026", "11", "20"]))       # 조각을 이어 붙인다
print(" ".join(words))
