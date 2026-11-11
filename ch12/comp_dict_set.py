names = ["이서연", "박준호", "최민지"]
scores = [92, 78, 85]

# 딕셔너리 컴프리헨션: 중괄호 안에 키: 값
table = {name: score for name, score in zip(names, scores)}
print(table)

high = {name: score for name, score in table.items() if score >= 80}
print(high)

# 집합 컴프리헨션: 중괄호 안에 값만
words = ["kiwi", "apple", "plum", "grape"]
print({len(word) for word in words})
