def fibonacci(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b     # 두 값을 한꺼번에 다음 단계로 옮긴다


print(list(fibonacci(10)))
