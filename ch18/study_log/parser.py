"""자유롭게 적은 한 줄에서 과목, 학습 시간, 점수를 읽어 낸다."""
import re

from .errors import RecordError

# 과목, 공백, 학습 시간, 그리고 있을 수도 있는 '85점'
ENTRY = re.compile(
    r"(?P<subject>\S+)\s+(?P<duration>.+?)(?:\s+(?P<score>\d+)점)?"
)

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
        raise RecordError(f"학습 시간이 아니다: {text}")
    hours = float(m.group("hours") or 0)
    minutes = int(m.group("minutes") or 0)
    return round(hours + minutes / 60, 2)


def parse_entry(text):
    """'파이썬 1시간 85점'을 ('파이썬', 1.0, 85)로 바꾼다.

    점수를 적지 않았으면 셋째 값은 None이다.
    """
    m = ENTRY.fullmatch(text.strip())
    if not m:
        raise RecordError(f"'과목 시간' 형식이 아니다: {text}")
    score = int(m.group("score")) if m.group("score") else None
    return m.group("subject"), parse_duration(m.group("duration")), score
