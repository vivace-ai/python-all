def logged(func):
    def wrapper():
        print("호출:", func.__name__)
        return func()

    return wrapper


@logged
def add(a, b):
    return a + b


print(add(2, 3))
