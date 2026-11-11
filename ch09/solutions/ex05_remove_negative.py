def without_negative(numbers):
    result = []
    for n in numbers:
        if n >= 0:
            result.append(n)
    return result


data = [12000, -3000, 8500, -500, 23000]
print(without_negative(data))
print(data)     # 원본은 바뀌지 않는다
