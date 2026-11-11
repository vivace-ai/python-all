from functools import wraps


def logged(func):
    @wraps(func)    # 원래 함수의 이름과 설명을 옮겨 준다
    def wrapper(*args, **kwargs):
        print(f"호출: {func.__name__}{args}")
        return func(*args, **kwargs)

    return wrapper


@logged
def add(a, b):
    """두 수를 더한다."""
    return a + b


print(add(2, 3))
print(add.__name__, "-", add.__doc__)
