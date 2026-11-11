def apply_twice(func, value):    # 함수를 인자로 받는다
    return func(func(value))


def add_ten(n):
    return n + 10


print(apply_twice(add_ten, 5))
