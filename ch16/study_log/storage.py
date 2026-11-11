"""기록을 파일에 쓰고 읽는 일을 맡는다."""
from .records import make_record


def load_records(path):
    """파일에서 기록을 읽는다. 읽지 못한 줄은 알리고 건너뛴다."""
    records = []
    try:
        with open(path, encoding="utf-8") as f:
            for number, line in enumerate(f, start=1):
                try:
                    day, subject, hours = line.strip().split("\t")
                    records.append(make_record(day, subject, hours))
                except ValueError:
                    print(f"[경고] {number}번째 줄을 건너뜁니다.")
    except FileNotFoundError:
        pass    # 첫 실행에는 파일이 없다. 빈 리스트로 시작한다
    return records


def append_record(path, record):
    """기록 한 건을 파일 끝에 한 줄로 덧붙인다."""
    line = f"{record['day']}\t{record['subject']}\t{record['hours']}\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(line)
