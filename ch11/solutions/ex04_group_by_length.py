words = ["kiwi", "apple", "fig", "grape", "plum", "pear", "banana"]

groups = {}
for word in words:
    length = len(word)
    if length not in groups:
        groups[length] = []
    groups[length].append(word)

for length in sorted(groups):   # 키를 작은 순서로
    print(length, groups[length])
