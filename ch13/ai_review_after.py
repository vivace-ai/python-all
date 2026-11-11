from pathlib import Path


def add_record(path, subject, hours):
    # 덧붙이는 모드로 열고, 인코딩을 적는다
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{subject},{hours}\n")


# 앞의 실행이 남긴 파일을 지우고 시작한다
Path("study.txt").unlink(missing_ok=True)
add_record("study.txt", "파이썬", 1.5)
add_record("study.txt", "통계학", 1.0)
add_record("study.txt", "글쓰기", 0.5)

with open("study.txt", encoding="utf-8") as f:
    print(f.read(), end="")
