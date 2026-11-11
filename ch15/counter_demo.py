from collections import Counter, defaultdict

words = "to be or not to be".split()

counts = Counter(words)                 # 세기
print(counts)
print(counts.most_common(2))            # 많이 나온 순서로 두 개
print(counts["be"], counts["python"])   # 없는 키는 0이다

groups = defaultdict(list)              # 묶기
for word in words:
    groups[len(word)].append(word)
print(dict(groups))
