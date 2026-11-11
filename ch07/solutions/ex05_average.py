def average(*numbers):
    if not numbers:     # 인자가 없으면 0으로 나누지 않도록 먼저 끝낸다
        return 0
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


print(average(80, 90, 70))
print(average(100))
print(average())
