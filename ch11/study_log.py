# 학습 기록 프로그램 5단계: 과목을 함께 기록하고 과목별로 집계한다


def read_record(day):
    """'과목 시간' 한 줄을 받아 기록 하나를 돌려준다. q면 None."""
    while True:
        text = input(f"{day}일차 (과목 시간) > ").strip()
        if text.lower() == "q":
            return None
        parts = text.split()
        if len(parts) != 2:
            print("'과목 시간' 형식으로 입력하세요. 예: 파이썬 1.5")
            continue
        subject, hours_text = parts
        hours = float(hours_text)
        if not 0 <= hours <= 24:
            print("시간은 0에서 24 사이로 입력하세요.")
            continue
        return {"day": day, "subject": subject, "hours": hours}


def read_records():
    """q를 입력할 때까지 받은 기록을 리스트로 돌려준다."""
    records = []
    while True:
        record = read_record(len(records) + 1)
        if record is None:
            return records
        records.append(record)


def total_by_subject(records):
    """과목을 키로, 그 과목의 총 학습 시간을 값으로 돌려준다."""
    totals = {}
    for record in records:
        subject = record["subject"]
        totals[subject] = totals.get(subject, 0) + record["hours"]
    return totals


def print_summary(records):
    if not records:
        print("기록이 없습니다.")
        return
    totals = total_by_subject(records)
    total = sum(totals.values())
    print(f"기록 {len(records)}건, 총 {total:.1f}시간")

    ranked = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    for subject, hours in ranked:
        bar = "■" * round(hours * 2)
        print(f"{subject} {bar} {hours:.1f}시간 ({hours / total:.0%})")


def main():
    print("과목과 시간을 입력하세요. 끝내려면 q")
    records = read_records()
    print()
    print_summary(records)


main()
