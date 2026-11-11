with open("sales.txt", "w", encoding="cp949") as f:
    f.write("매출 보고\n")

with open("sales.txt", encoding="utf-8") as f:
    print(f.read())
