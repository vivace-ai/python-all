a = [1, 2, 3]
b = a           # 같은 리스트에 이름을 하나 더 붙인다

b.append(4)
print(a)        # a도 바뀌었다
print(a is b)   # 두 이름이 같은 리스트를 가리킨다
