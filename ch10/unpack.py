point = (3, 4)
x, y = point                            # 항목을 이름에 하나씩 나눠 담는다
print(x, y)

name, age, city = "이서연", 34, "서울"  # 오른쪽은 튜플이다
print(name, age, city)

first, *rest = [72, 95, 48, 61]         # 별표가 나머지를 받는다
print(first, rest)
