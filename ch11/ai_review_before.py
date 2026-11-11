# AI가 내놓은 코드: 학생을 등급별로 나눈다
students = [("이서연", "A"), ("박준호", "B"),
            ("최민지", "A"), ("정도윤", "C")]

groups = dict.fromkeys(["A", "B", "C"], [])
for name, grade in students:
    groups[grade].append(name)

for grade, names in groups.items():
    print(grade, names)
