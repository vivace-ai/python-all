import re

RULES = [
    (r".{8,}", "8자 이상이어야 한다"),
    (r"[A-Za-z]", "영문자가 있어야 한다"),
    (r"\d", "숫자가 있어야 한다"),
    (r"[^\w\s]", "특수문자가 있어야 한다"),
]


def check(password):
    """지키지 못한 규칙의 설명을 리스트로 돌려준다."""
    return [reason for pattern, reason in RULES
            if not re.search(pattern, password)]


for password in ["python", "python2026", "Py!thon2026"]:
    problems = check(password)
    print(password, "->", problems if problems else "통과")
