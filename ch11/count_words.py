text = "the quick brown fox jumps over the lazy dog and the quick cat"

counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1  # 없으면 0에서 시작한다

print(counts["the"], counts["quick"], counts["fox"])
print(max(counts, key=counts.get))          # 가장 많이 나온 낱말
