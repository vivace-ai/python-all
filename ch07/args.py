def total(*amounts):    # 인자를 몇 개든 받는다
    result = 0
    for amount in amounts:
        result += amount
    return result


print(total(1000, 2000))
print(total(1000, 2000, 3000, 4000))
print(total())
