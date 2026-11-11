tasks = ["메일", "회의", "보고서", "회의"]

tasks.remove("회의")    # 값으로 지운다. 처음 나오는 것 하나만
print(tasks)

last = tasks.pop()      # 마지막 항목을 꺼내면서 지운다
print(last, tasks)

first = tasks.pop(0)    # 인덱스를 주면 그 자리의 항목을 꺼낸다
print(first, tasks)
