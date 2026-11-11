numbers = [1, 2, 2, 3]

for n in numbers:
    if n == 2:
        numbers.remove(n)   # 순회하는 리스트에서 지운다

print(numbers)              # 2가 하나 남았다
