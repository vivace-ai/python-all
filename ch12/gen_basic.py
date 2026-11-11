def countdown(n):
    while n > 0:
        yield n     # 값을 하나 내주고 여기서 멈춘다
        n -= 1


for number in countdown(3):
    print(number)

gen = countdown(2)
print(next(gen), next(gen))
