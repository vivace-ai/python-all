from logtools import logged


def multiply(a, b):
    return a * b


multiply = logged(multiply)     # @logged가 하는 일을 손으로 한 것
print(multiply(4, 5))
