filename = input("파일 이름: ")

position = filename.rfind(".")  # 마지막 마침표의 위치
if position == -1:
    print("확장자가 없습니다.")
else:
    print(f"이름: {filename[:position]}")
    print(f"확장자: {filename[position + 1:]}")
