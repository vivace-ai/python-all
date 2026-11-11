# 학습 기록 프로그램 6단계: 고르고 집계하는 함수를 컴프리헨션으로 쓴다

RECORDS = [
    {"day": 1, "subject": "파이썬", "hours": 1.5},
    {"day": 2, "subject": "통계학", "hours": 1.0},
    {"day": 3, "subject": "파이썬", "hours": 2.0},
    {"day": 4, "subject": "글쓰기", "hours": 0.5},
    {"day": 5, "subject": "파이썬", "hours": 1.0},
    {"day": 6, "subject": "통계학", "hours": 2.5},
]


def subjects(records):
    """기록에 나온 과목을 사전 순서로 돌려준다."""
    return sorted({r["subject"] for r in records})


def hours_of(records, subject):
    """한 과목의 총 학습 시간을 돌려준다."""
    return sum(r["hours"] for r in records if r["subject"] == subject)


def totals(records):
    """과목별 총 학습 시간을 딕셔너리로 돌려준다."""
    return {s: hours_of(records, s) for s in subjects(records)}


def long_days(records, minimum):
    """minimum시간 이상 공부한 날의 번호를 돌려준다."""
    return [r["day"] for r in records if r["hours"] >= minimum]


print(subjects(RECORDS))
print(totals(RECORDS))
print(long_days(RECORDS, 2))
print(max(RECORDS, key=lambda r: r["hours"]))
