def distance(p, q):
    x1, y1 = p  # 좌표를 풀어 담는다
    x2, y2 = q
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


print(distance((0, 0), (3, 4)))
print(f"{distance((1, 2), (4, 6)):.1f}")
