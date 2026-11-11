# 학습 기록 프로그램 9단계: 일을 모듈로 나누고 외부 라이브러리를 쓴다
from pathlib import Path

from study_log.records import make_record
from study_log.report import summary_table
from study_log.storage import append_record, load_records

DATA_FILE = Path(__file__).parent / "study_log.txt"


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
            return make_record(day, parts[0], parts[1])
        except ValueError:
            print("시간은 0에서 24 사이의 숫자로 입력하세요.")


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
