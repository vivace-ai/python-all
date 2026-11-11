# 학습 기록 프로그램 10단계: 자유롭게 적은 학습 시간을 읽어 낸다
from pathlib import Path

from study_log.parser import parse_entry
from study_log.records import make_record
from study_log.report import summary_table
from study_log.storage import append_record, load_records

DATA_FILE = Path(__file__).parent / "study_log.txt"


def read_record(day):
    """한 줄을 받아 기록 하나를 돌려준다. q면 None."""
    while True:
        text = input(f"{day}일차 > ").strip()
        if text.lower() == "q":
            return None
        try:
            subject, hours = parse_entry(text)
            return make_record(day, subject, hours)
        except ValueError:
            print("예: 파이썬 1시간 30분, 통계학 2h, 글쓰기 45분")


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
    print(summary_table(records))


if __name__ == "__main__":
    main()
