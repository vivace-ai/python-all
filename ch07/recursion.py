def factorial(n):
    if n <= 1:                      # 종료 조건: 더 부르지 않는다
        return 1
    return n * factorial(n - 1)     # 자기 자신을 부른다


print(factorial(4))
print(factorial(10))
