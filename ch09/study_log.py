# 학습 기록 프로그램 4단계: 날짜별 기록을 리스트에 보관한다


def read_hours(day):
    """하루 학습 시간을 입력받는다. q를 입력하면 None을 돌려준다."""
    while True:
        text = input(f"{day}일차 (시간) > ").strip().lower()
        if text == "q":
            return None
        hours = float(text)
        if 0 <= hours <= 24:
            return hours
        print("0에서 24 사이로 입력하세요.")


def read_records():
    """q를 입력할 때까지 받은 기록을 리스트로 돌려준다."""
    records = []
    while True:
        hours = read_hours(len(records) + 1)
        if hours is None:
            return records
        records.append(hours)


def print_chart(records):
    """날짜별 기록을 막대그래프로 출력한다. 30분이 한 칸이다."""
    for day, hours in enumerate(records, start=1):
        bar = "■" * round(hours * 2)
        print(f"{day:>2}일차 {bar} {hours:.1f}")


def print_summary(records):
    """합계, 평균, 최장 기록, 최근 3일 평균을 출력한다."""
    if not records:
        print("기록이 없습니다.")
        return
    total = sum(records)
    longest = max(records)
    best_day = records.index(longest) + 1
    recent = records[-3:]   # 3일이 안 되면 있는 만큼만

    print(f"기록한 날   {len(records)}일")
    print(f"총 학습     {total:.1f}시간")
    print(f"하루 평균   {total / len(records):.1f}시간")
    print(f"최장 기록   {longest:.1f}시간 ({best_day}일차)")
    print(f"최근 평균   {sum(recent) / len(recent):.1f}시간")


def main():
    print("하루 학습 시간을 입력하세요. 끝내려면 q")
    records = read_records()
    print()
    print_chart(records)
    print()
    print_summary(records)


main()
