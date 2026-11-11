from tabulate import tabulate

rows = [["파이썬", 4.5], ["통계학", 3.5], ["글쓰기", 0.5]]
print(tabulate(rows, headers=["과목", "시간"]))
