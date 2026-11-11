# AI가 내놓은 코드: 기록 한 건을 파일에 추가한다
def add_record(path, subject, hours):
    with open(path, "w") as f:
        f.write(f"{subject},{hours}\n")


add_record("study.txt", "파이썬", 1.5)
add_record("study.txt", "통계학", 1.0)
add_record("study.txt", "글쓰기", 0.5)

with open("study.txt") as f:
    print(f.read(), end="")
