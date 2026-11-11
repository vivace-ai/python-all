stock = {"키보드": 12, "마우스": 0}

print(stock.get("키보드"))      # 있으면 값을 돌려준다
print(stock.get("모니터"))      # 없으면 None을 돌려준다
print(stock.get("모니터", 0))   # 없을 때 쓸 값을 정할 수 있다

if "모니터" in stock:           # 있는지 먼저 확인하는 방법
    print(stock["모니터"])
else:
    print("취급하지 않는 상품입니다.")
