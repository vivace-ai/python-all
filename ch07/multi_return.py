def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)   # 쉼표로 나열해 두 값을 돌려준다


lowest, highest = min_max(72, 95, 68)
print(f"최저 {lowest}, 최고 {highest}")
