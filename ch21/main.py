# 학습 기록 프로그램 15단계: 기록을 웹 API 너머의 서버에 보관한다
import requests

from study_log.errors import RecordError
from study_log.log import StudyLog
from study_log.parser import parse_entry
from study_log.report import exam_summary, summary_table
from study_log.storage_remote import RemoteStorage

SERVER = "http://127.0.0.1:8021"


def main() -> None:
    try:
        log = StudyLog(RemoteStorage(SERVER))
    except requests.RequestException:
        print("서버에 연결할 수 없습니다. ch21/server.py를 먼저 실행하세요.")
        return
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
