"""다른 파일에서 가져다 쓰는 데코레이터 모음."""
from functools import wraps


def logged(func):
    """함수가 불릴 때마다 호출과 결과를 출력하게 만든다."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"호출: {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"결과: {result}")
        return result

    return wrapper
