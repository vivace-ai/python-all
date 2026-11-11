def make_multiplier(factor):
    def multiply(n):
        return n * factor   # 바깥 함수의 변수 factor를 기억한다

    return multiply         # 함수를 호출하지 않고 그대로 돌려준다


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5), triple(5))
print(double.__name__)
