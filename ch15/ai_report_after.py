def make_report(totals):
    """과목별 학습 시간을 보고서 문자열로 만든다."""
    lines = [f"{name}: {hours:.1f}시간" for name, hours in totals.items()]
    return "\n".join(lines)


if __name__ == "__main__":
    sample = {"파이썬": 4.5, "통계학": 3.5}
    print("=== 테스트 ===")
    print(make_report(sample))
