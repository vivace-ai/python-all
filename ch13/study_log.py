# 학습 기록 프로그램 7단계: 기록을 파일에 저장하고 다시 읽어 온다
from pathlib import Path

DATA_FILE = Path(__file__).parent / "study_log.txt"


def load_records(path):
    """파일에서 기록을 읽어 돌려준다. 파일이 없으면 빈 리스트다."""
    if not path.exists():
        return []
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            day, subject, hours = line.strip().split("\t")
            records.append(
                {"day": int(day), "subject": subject, "hours": float(hours)}
            )
    return records


def append_record(path, record):
    """기록 한 건을 파일 끝에 한 줄로 덧붙인다."""
    line = f"{record['day']}\t{record['subject']}\t{record['hours']}\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(line)


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


def total_by_subject(records):
    """과목을 키로, 그 과목의 총 학습 시간을 값으로 돌려준다."""
    totals = {}
    for record in records:
        subject = record["subject"]
        totals[subject] = totals.get(subject, 0) + record["hours"]
    return totals


def main():
    records = load_records(DATA_FILE)
    print(f"저장된 기록 {len(records)}건을 불러왔습니다. 끝내려면 q")
    while True:
        record = read_record(len(records) + 1)
        if record is None:
            break
        records.append(record)
        append_record(DATA_FILE, record)    # 받는 즉시 저장한다

    print()
    for subject, hours in total_by_subject(records).items():
        print(f"{subject} {hours:.1f}시간")


main()
