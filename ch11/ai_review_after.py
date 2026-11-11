students = [("이서연", "A"), ("박준호", "B"),
            ("최민지", "A"), ("정도윤", "C")]

groups = {}
for grade in ["A", "B", "C"]:
    groups[grade] = []  # 등급마다 리스트를 새로 만든다

for name, grade in students:
    groups[grade].append(name)

for grade, names in groups.items():
    print(grade, names)
