from functools import wraps


def logged(func):
    @wraps(func)                        # 이름과 설명을 지킨다
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 실행")
        return func(*args, **kwargs)    # 결과를 돌려준다

    return wrapper


@logged
def add_tax(price):
    """부가세를 더한 가격을 돌려준다."""
    return round(price * 1.1)


total = add_tax(10000)
print(total)
print(add_tax.__name__, "-", add_tax.__doc__)
