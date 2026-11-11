import sys


class Collector:
    """파일처럼 write()를 받아, 받은 문자열을 모아 두는 객체."""

    def __init__(self):
        self.lines = []

    def write(self, text):
        self.lines.append(text)


def write_report(out, totals):
    """out이 무엇이든 write()만 있으면 된다."""
    for subject, hours in totals.items():
        out.write(f"{subject} {hours}시간\n")


totals = {"파이썬": 3.5, "통계학": 2.0}

write_report(sys.stdout, totals)    # 화면에 쓴다
collector = Collector()
write_report(collector, totals)     # 내가 만든 객체에 쓴다
print(collector.lines)
