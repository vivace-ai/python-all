table = [
    [80, 90, 70],
    [65, 85, 95],
    [75, 60, 88],
]

for row in table:
    print(f"행 합계: {sum(row)}")

for col in range(len(table[0])):
    total = 0
    for row in table:
        total += row[col]   # 행마다 같은 자리의 값을 더한다
    print(f"{col}번 열 합계: {total}")
