def merge(a, b):
    result = a.copy()   # a를 바꾸지 않도록 복사해 둔다
    for name, count in b.items():
        result[name] = result.get(name, 0) + count
    return result


seoul = {"키보드": 12, "마우스": 30}
busan = {"마우스": 15, "모니터": 4}
print(merge(seoul, busan))
print(seoul)            # 원본은 그대로다
