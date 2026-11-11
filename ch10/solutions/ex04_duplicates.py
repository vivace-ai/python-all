def duplicates(words):
    seen = set()
    repeated = set()
    for word in words:
        if word in seen:
            repeated.add(word)  # 이미 본 낱말이면 중복이다
        seen.add(word)
    return sorted(repeated)


text = "the quick brown fox jumps over the lazy dog and the quick cat"
print(duplicates(text.split()))
