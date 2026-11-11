records = [("이서연", 92), ("박준호", 78), ("최민지", 85)]

for name, score in records:                         # 돌 때마다 풀어 받는다
    print(f"{name}: {score}점")

best = max(records, key=lambda record: record[1])   # 점수 기준
print(best)
