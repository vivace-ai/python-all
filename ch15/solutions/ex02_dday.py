from datetime import date

today = date(2026, 11, 2)
exam = date(2027, 3, 14)

remaining = (exam - today).days
print(f"시험까지 {remaining}일 남았습니다.")
print(f"{remaining // 7}주 {remaining % 7}일입니다.")
