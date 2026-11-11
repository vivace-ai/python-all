stock = {"키보드": 3}

# 방법 1: 먼저 확인하고 꺼낸다
if "마우스" in stock:
    print(stock["마우스"])
else:
    print("없는 상품입니다.")

# 방법 2: 일단 꺼내고, 안 되면 수습한다
try:
    print(stock["마우스"])
except KeyError:
    print("없는 상품입니다.")
