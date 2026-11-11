text = "programming is fun and python is powerful"

counts = {}
for ch in text.replace(" ", ""):    # 공백은 세지 않는다
    counts[ch] = counts.get(ch, 0) + 1

top3 = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:3]
for ch, count in top3:
    print(f"{ch}: {count}번")
