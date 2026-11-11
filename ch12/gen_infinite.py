def naturals():
    n = 1
    while True:     # 끝이 없는 수열
        yield n
        n += 1


for n in naturals():
    if n * n > 50:  # 제곱이 50을 넘는 첫 자연수
        break
print(n)
