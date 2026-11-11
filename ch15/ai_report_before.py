# AI가 내놓은 모듈: 과목별 학습 시간을 보고서 문자열로 만든다
def make_report(totals):
    lines = [f"{name}: {hours:.1f}시간" for name, hours in totals.items()]
    return "\n".join(lines)


# 테스트
sample = {"파이썬": 4.5, "통계학": 3.5}
print("=== 테스트 ===")
print(make_report(sample))
