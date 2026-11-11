prices = {"키보드": 89000, "마우스": 35000, "모니터": 420000}

for name in prices:                 # 딕셔너리를 돌면 키가 나온다
    print(name)

for name, price in prices.items():  # 키와 값을 함께 꺼낸다
    print(f"{name}: {price:,}원")

print(sum(prices.values()))         # 값만 모아 합계를 낸다
print(list(prices.keys()))
