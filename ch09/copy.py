a = [1, 2, 3]
b = a.copy()    # 내용이 같은 새 리스트를 만든다

b.append(4)
print(a, b)
print(a is b)
