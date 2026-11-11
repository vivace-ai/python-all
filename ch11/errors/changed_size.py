stock = {"키보드": 12, "마우스": 0, "모니터": 3}

for name in stock:
    if stock[name] == 0:
        del stock[name]     # 순회하는 딕셔너리에서 지운다
