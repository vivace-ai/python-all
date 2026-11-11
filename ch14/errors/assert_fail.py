def average(values):
    assert len(values) > 0, "평균을 낼 값이 없다"
    return sum(values) / len(values)


print(average([3, 4]))
print(average([]))
