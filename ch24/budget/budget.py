"""지출 요약 도구. 명세는 SPEC.md에 있다."""
import csv
from pathlib import Path


def parse_amount(text: str) -> int | None:
    """금액 문자열을 정수로 바꾼다. 바꿀 수 없으면 None."""
    cleaned = text.replace(",", "").strip()
    if not cleaned.isdigit():
        return None
    return int(cleaned)


def read_rows(path: Path) -> list[dict]:
    """CSV 파일의 행을 딕셔너리의 리스트로 읽는다."""
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def summarize(rows: list[dict]) -> tuple[dict[str, int], int]:
    """항목별 합계와 건너뛴 행의 수를 돌려준다."""
    totals: dict[str, int] = {}
    skipped = 0
    for row in rows:
        amount = parse_amount(row["amount"])
        if amount is None:
            skipped += 1
            continue
        category = row["category"]
        totals[category] = totals.get(category, 0) + amount
    return totals, skipped


def report(totals: dict[str, int], skipped: int) -> list[str]:
    """출력할 글을 줄의 리스트로 만든다. 금액이 큰 항목이 먼저다."""
    ranked = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    lines = [f"{category}: {amount:,}원" for category, amount in ranked]
    lines.append(f"합계: {sum(totals.values()):,}원")
    if skipped:
        lines.append(f"금액을 읽지 못해 건너뛴 행: {skipped}개")
    return lines


if __name__ == "__main__":
    rows = read_rows(Path(__file__).parent / "expenses.csv")
    totals, skipped = summarize(rows)
    print("\n".join(report(totals, skipped)))
