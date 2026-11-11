prices = {"키보드": 89000, "마우스": 35000, "모니터": 420000}

sale = {name: int(price * 0.8) for name, price in prices.items()}
print(sale)

cheap = {name: price for name, price in sale.items() if price < 100000}
print(cheap)
