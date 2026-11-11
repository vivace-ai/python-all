# 학습 기록 프로그램 8단계: 잘못된 입력과 깨진 파일에도 멈추지 않는다
from pathlib import Path

DATA_FILE = Path(__file__).parent / "study_log.txt"


def check_hours(hours):
    """학습 시간으로 쓸 수 있는 값인지 확인하고 그대로 돌려준다."""
    if not 0 <= hours <= 24:
        raise ValueError(f"시간은 0에서 24 사이여야 한다: {hours}")
    return hours


def parse_line(line):
    """파일의 한 줄을 기록으로 바꾼다. 형식이 틀리면 ValueError가 난다."""
    day, subject, hours = line.strip().split("\t")
    return {"day": int(day), "subject": subject,
            "hours": check_hours(float(hours))}


def load_records(path):
    """파일에서 기록을 읽는다. 읽지 못한 줄은 알리고 건너뛴다."""
    records = []
    try:
        with open(path, encoding="utf-8") as f:
            for number, line in enumerate(f, start=1):
                try:
                    records.append(parse_line(line))
                except ValueError:
                    text = line.strip()
                    print(f"[경고] {number}번째 줄을 건너뜁니다: {text}")
    except FileNotFoundError:
        pass    # 첫 실행에는 파일이 없다. 빈 리스트로 시작한다
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
        try:
            hours = check_hours(float(parts[1]))
        except ValueError:
            print("시간은 0에서 24 사이의 숫자로 입력하세요.")
            continue
        return {"day": day, "subject": parts[0], "hours": hours}


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
    day = records[-1]["day"] + 1 if records else 1
    while True:
        record = read_record(day)
        if record is None:
            break
        records.append(record)
        append_record(DATA_FILE, record)
        day += 1

    print()
    for subject, hours in total_by_subject(records).items():
        print(f"{subject} {hours:.1f}시간")


main()
