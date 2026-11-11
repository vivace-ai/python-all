def logged(func):
    def wrapper(*args, **kwargs):
        print("호출:", func.__name__)
        return func(*args, **kwargs)


@logged
def add(a, b):
    return a + b


print(add(2, 3))
