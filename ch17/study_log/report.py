"""기록을 표로 만드는 일을 맡는다."""
from tabulate import tabulate


def summary_table(log):
    """과목별 합계를 시간이 많은 순서의 표로 만든다."""
    rows = log.total_by_subject().most_common()
    return tabulate(rows, headers=["과목", "시간"], floatfmt=".1f")
