"""기록을 집계하고 표로 만드는 일을 맡는다."""
from collections import Counter

from tabulate import tabulate


def total_by_subject(records):
    """과목을 키로, 그 과목의 총 학습 시간을 값으로 돌려준다."""
    totals = Counter()
    for record in records:
        totals[record["subject"]] += record["hours"]
    return totals


def summary_table(records):
    """과목별 합계를 시간이 많은 순서의 표로 만든다."""
    rows = total_by_subject(records).most_common()
    return tabulate(rows, headers=["과목", "시간"], floatfmt=".1f")
