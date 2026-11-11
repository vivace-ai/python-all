# 학습 기록 프로그램 11단계: 기록과 기록 모음을 클래스로 나타낸다
from pathlib import Path

from study_log.log import StudyLog
from study_log.parser import parse_entry
from study_log.report import summary_table

DATA_FILE = Path(__file__).parent / "study_log.txt"


def main():
    log = StudyLog(DATA_FILE)
    print(f"저장된 기록 {len(log)}건을 불러왔습니다. 끝내려면 q")
    while True:
        text = input(f"{log.next_day}일차 > ").strip()
        if text.lower() == "q":
            break
        try:
            subject, hours = parse_entry(text)
            record = log.add(subject, hours)
        except ValueError:
            print("  다시 입력하세요. 예: 파이썬 1시간 30분, 통계학 2h")
            continue
        print(f"  기록했습니다: {record}")

    print()
    print(summary_table(log))


if __name__ == "__main__":
    main()
