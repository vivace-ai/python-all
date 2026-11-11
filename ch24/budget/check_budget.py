# 지출 요약 도구가 지켜야 할 것. 명세의 문장을 하나씩 옮겼다
from budget import parse_amount, report, summarize

assert parse_amount("12000") == 12000
assert parse_amount("8,500") == 8500    # 쉼표가 든 금액
assert parse_amount("") is None         # 빈 칸
assert parse_amount("만 원") is None    # 숫자가 아니다

rows = [
    {"category": "교통", "amount": "1450"},
    {"category": "식비", "amount": "12000"},
    {"category": "식비", "amount": "8,500"},
    {"category": "식비", "amount": ""},
]
totals, skipped = summarize(rows)
assert totals == {"교통": 1450, "식비": 20500}
assert skipped == 1

# 실제 파일을 실행해 보고 나서 더한 확인: 금액이 큰 항목이 먼저 나온다
assert report(totals, skipped)[0] == "식비: 20,500원"
print("모든 확인을 통과했습니다.")
