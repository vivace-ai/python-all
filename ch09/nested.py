table = [
    [80, 90, 70],                           # 0번 행: 1반의 세 과목 점수
    [65, 85, 95],                           # 1번 행: 2반의 세 과목 점수
]

print(table[1])                             # 행 하나가 리스트다
print(table[1][2])                          # 1번 행의 2번 항목

for row in table:
    print(f"{sum(row) / len(row):.1f}")     # 행마다 평균을 낸다
