# 학습 기록 프로그램 2단계: 며칠 치 기록을 이어서 입력받는다
print("하루 학습 시간을 입력하세요. 끝내려면 q")

days = 0        # 기록한 날 수
total = 0.0     # 누적 시간
longest = 0.0   # 가장 오래 공부한 날

while True:
    text = input(f"{days + 1}일차 (시간) > ")
    if text == "q":
        break

    hours = float(text)
    if hours < 0 or hours > 24:
        print("0에서 24 사이로 입력하세요.")
        continue

    days += 1
    total += hours
    if hours > longest:
        longest = hours

if days == 0:
    print("기록이 없습니다.")
else:
    print()
    print(f"기록한 날   {days}일")
    print(f"총 학습     {total:.1f}시간")
    print(f"하루 평균   {total / days:.1f}시간")
    print(f"최장 기록   {longest:.1f}시간")
