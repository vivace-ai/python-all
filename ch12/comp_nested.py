table = [[80, 90, 70], [65, 85, 95]]

# 행마다 평균을 낸다
print([round(sum(row) / len(row), 1) for row in table])

# for를 두 번 써서 한 줄로 펼친다
print([value for row in table for value in row])

# 돌 때마다 새 행을 만든다
grid = [[0] * 3 for _ in range(2)]
grid[0][0] = 9
print(grid)
