# 학습 기록 프로그램 13단계: 타입 힌트를 붙이고 보관소를 건네받는다
from pathlib import Path

from study_log.errors import RecordError
from study_log.log import StudyLog
from study_log.parser import parse_entry
from study_log.report import exam_summary, summary_table
from study_log.storage import FileStorage

DATA_FILE = Path(__file__).parent / "study_log.txt"


def main() -> None:
    log = StudyLog(FileStorage(DATA_FILE))  # 파일 보관소를 건네준다
    print(f"저장된 기록 {len(log)}건을 불러왔습니다. 끝내려면 q")
    while True:
        text = input(f"{log.next_day}일차 > ").strip()
        if text.lower() == "q":
            break
        try:
            subject, hours, score = parse_entry(text)
            record = log.add(subject, hours, score)
        except RecordError:
            print("  예: 파이썬 1시간 30분, 통계학 1h 85점")
            continue
        print(f"  기록했습니다: {record}")

    print()
    print(summary_table(log))
    if exam_summary(log):
        print(exam_summary(log))


if __name__ == "__main__":
    main()
