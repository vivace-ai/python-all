# 학습 기록 프로그램 3단계: 입력, 판단, 출력을 함수로 나눈다


def read_hours(day):
    """하루 학습 시간을 입력받는다. q를 입력하면 None을 돌려준다."""
    while True:
        text = input(f"{day}일차 (시간) > ")
        if text == "q":
            return None
        hours = float(text)
        if 0 <= hours <= 24:
            return hours
        print("0에서 24 사이로 입력하세요.")


def comment_for(hours):
    """학습 시간에 맞는 한 줄 평을 돌려준다."""
    if hours == 0:
        return "쉬어 가는 날"
    if hours < 1:
        return "짧게라도 이어 간 날"
    if hours < 3:
        return "꾸준한 속도"
    return "집중한 하루"


def print_summary(days, total, longest):
    """기록한 날 수, 총 시간, 평균, 최장 기록을 출력한다."""
    if days == 0:
        print("기록이 없습니다.")
        return
    print()
    print(f"기록한 날   {days}일")
    print(f"총 학습     {total:.1f}시간")
    print(f"하루 평균   {total / days:.1f}시간")
    print(f"최장 기록   {longest:.1f}시간")


def main():
    print("하루 학습 시간을 입력하세요. 끝내려면 q")
    days, total, longest = 0, 0.0, 0.0

    while True:
        hours = read_hours(days + 1)
        if hours is None:
            break
        print(f"  -> {comment_for(hours)}")
        days += 1
        total += hours
        longest = max(longest, hours)

    print_summary(days, total, longest)


main()
