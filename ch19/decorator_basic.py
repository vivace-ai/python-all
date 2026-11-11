def logged(func):
    """함수가 불릴 때마다 호출과 결과를 출력하게 만든다."""

    def wrapper(*args, **kwargs):
        print(f"호출: {func.__name__}{args}")
        result = func(*args, **kwargs)  # 원래 함수를 부른다
        print(f"결과: {result}")
        return result                   # 결과를 그대로 돌려준다

    return wrapper


@logged
def add(a, b):
    return a + b


total = add(2, 3)
print(total)
