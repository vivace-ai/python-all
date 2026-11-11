grid = [[0] * 3] * 2        # 같은 행을 두 번 가리키는 리스트
grid[0][0] = 9
print(grid)

grid = []
for _ in range(2):
    grid.append([0] * 3)    # 돌 때마다 새 행을 만든다
grid[0][0] = 9
print(grid)
