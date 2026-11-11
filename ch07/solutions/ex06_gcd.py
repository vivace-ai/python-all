def gcd(a, b):
    if b == 0:              # 종료 조건
        return a
    return gcd(b, a % b)    # 더 작은 문제로 바꿔 다시 부른다


print(gcd(48, 18))
print(gcd(17, 5))
print(gcd(1071, 462))
