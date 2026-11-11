prices = {"키보드": 89000, "마우스": 35000, "모니터": 420000}

by_price = sorted(prices.items(), key=lambda item: item[1], reverse=True)
for name, price in by_price:        # 값이 큰 순서로
    print(f"{name}: {price:,}원")

print(min(prices, key=prices.get))  # 값이 가장 작은 키
