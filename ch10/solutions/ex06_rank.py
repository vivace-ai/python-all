records = [("이서연", 92), ("박준호", 78), ("최민지", 85), ("정도윤", 92)]

ordered = sorted(records, key=lambda record: record[1], reverse=True)
for rank, (name, score) in enumerate(ordered, start=1):
    print(f"{rank}위 {name} {score}점")
