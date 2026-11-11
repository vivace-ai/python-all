scores = [72, 95, 48, 61, 88]

# 뒤에 붙인 if: 조건에 맞는 항목만 고른다
passed = [s for s in scores if s >= 60]
print(passed)

# 앞에 쓴 조건 표현식: 항목마다 값을 바꾼다
labels = ["합격" if s >= 60 else "불합격" for s in scores]
print(labels)

# 식 자리에는 메서드 호출도 올 수 있다
names = ["  seoyeon ", "JUNHO", " minji"]
print([name.strip().title() for name in names])
