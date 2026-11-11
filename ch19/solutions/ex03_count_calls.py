from functools import wraps


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0   # 함수에도 속성을 붙일 수 있다
    return wrapper


@count_calls
def greet(name):
    return f"안녕하세요, {name} 님"


print(greet("이서연"))
print(greet("박준호"))
print(greet.__name__, greet.calls)
