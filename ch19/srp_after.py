def summarize(hours):
    """계산만 한다. 결과를 딕셔너리로 돌려준다."""
    total = sum(hours)
    return {"total": total, "average": total / len(hours)}


def as_sentence(summary):
    """표현만 한다. 문장으로 만든다."""
    total, average = summary["total"], summary["average"]
    return f"총 {total}시간, 하루 평균 {average:.1f}시간"


def as_markdown(summary):
    """같은 계산 결과를 다른 모양으로 표현한다."""
    total, average = summary["total"], summary["average"]
    return f"| 합계 | {total} |\n| 평균 | {average:.1f} |"


summary = summarize([1.5, 2.0, 0.5])
print(as_sentence(summary))
print(as_markdown(summary))
