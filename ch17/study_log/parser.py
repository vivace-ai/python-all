"""자유롭게 적은 한 줄에서 과목과 학습 시간을 읽어 낸다."""
import re

# 과목, 공백, 나머지
ENTRY = re.compile(r"(\S+)\s+(.+)")

# 1 또는 1.5
NUMBER = re.compile(r"\d+(?:\.\d+)?")

DURATION = re.compile(r"""
    (?: (?P<hours>\d+(?:\.\d+)?) \s* (?:시간|h) )?  # 1시간, 1.5h
    \s*
    (?: (?P<minutes>\d+) \s* (?:분|m) )?            # 30분, 45m
""", re.VERBOSE)


def parse_duration(text):
    """'1시간 30분', '2h', '45분', '1.5'를 시간 단위의 수로 바꾼다."""
    text = text.strip().lower()
    if NUMBER.fullmatch(text):
        return float(text)                          # 단위가 없으면 시간이다
    m = DURATION.fullmatch(text)
    if not m or not (m.group("hours") or m.group("minutes")):
        raise ValueError(f"학습 시간이 아니다: {text}")
    hours = float(m.group("hours") or 0)
    minutes = int(m.group("minutes") or 0)
    return round(hours + minutes / 60, 2)


def parse_entry(text):
    """'파이썬 1시간 30분'을 ('파이썬', 1.5)로 바꾼다."""
    m = ENTRY.fullmatch(text.strip())
    if not m:
        raise ValueError(f"'과목 시간' 형식이 아니다: {text}")
    return m.group(1), parse_duration(m.group(2))
