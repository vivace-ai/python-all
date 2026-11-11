import re
from collections import Counter
from pathlib import Path

LINE = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<level>[A-Z]+) (?P<message>.+)"
)

path = Path(__file__).parent.parent / "data" / "access.log"

levels = Counter()
errors = []
with open(path, encoding="utf-8") as f:
    for line in f:
        m = LINE.fullmatch(line.strip())
        if not m:
            continue
        levels[m.group("level")] += 1
        if m.group("level") == "ERROR":
            errors.append((m.group("time"), m.group("message")))

print(dict(levels))
for time, message in errors:
    print(time, message)
