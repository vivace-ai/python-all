prices = {"키보드": 89000, "마우스": 35000}

prices["모니터"] = 420000       # 없는 키에 대입하면 새로 들어간다
prices["마우스"] = 32000        # 있는 키에 대입하면 값이 바뀐다
print(prices)

del prices["키보드"]            # 키를 지운다
removed = prices.pop("모니터")  # 꺼내면서 지운다
print(removed, prices)
