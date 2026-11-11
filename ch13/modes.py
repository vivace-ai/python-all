# w: 새로 쓴다
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("첫째 줄\n")

# 다시 w: 앞의 내용이 사라진다
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("둘째 줄\n")

# a: 끝에 덧붙인다
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("셋째 줄\n")

# 모드를 생략하면 r: 읽는다
with open("log.txt", encoding="utf-8") as f:
    print(f.read(), end="")
