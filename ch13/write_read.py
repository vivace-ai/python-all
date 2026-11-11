with open("memo.txt", "w", encoding="utf-8") as f:
    f.write("파이썬 1.5시간\n")
    f.write("통계학 1시간\n")

with open("memo.txt", encoding="utf-8") as f:
    text = f.read()

print(text, end="")
print(repr(text))
