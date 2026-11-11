def read_int(prompt):
    """정수를 입력할 때까지 다시 묻는다."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("정수로 입력해 주세요.")


age = read_int("나이: ")
print(f"내년에는 {age + 1}세입니다.")
