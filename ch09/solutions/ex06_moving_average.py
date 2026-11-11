def moving_average(values, size=3):
    result = []
    for i in range(len(values) - size + 1):
        window = values[i:i + size]     # size개씩 잘라 낸 구간
        result.append(round(sum(window) / size, 1))
    return result


print(moving_average([1.5, 2.0, 0.5, 3.0, 2.5]))
print(moving_average([10, 20, 30, 40], size=2))
