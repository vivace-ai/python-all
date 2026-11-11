# AI가 내놓은 코드: 함수가 실행될 때마다 기록을 남기는 데코레이터
def logged(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 실행")
        func(*args, **kwargs)

    return wrapper


@logged
def add_tax(price):
    """부가세를 더한 가격을 돌려준다."""
    return round(price * 1.1)


total = add_tax(10000)
print(total)
print(add_tax.__name__, "-", add_tax.__doc__)
