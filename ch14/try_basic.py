text = input("오늘 공부한 시간: ")

try:
    hours = float(text)
    print(f"{hours}시간을 기록했습니다.")
except ValueError:
    print("숫자로 입력해 주세요.")

print("프로그램을 계속합니다.")
