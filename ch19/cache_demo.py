from functools import cache


@cache  # 같은 인자로 다시 부르면 계산하지 않고 기억한 값을 준다
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print(fib(80))
print(fib.cache_info().currsize)
