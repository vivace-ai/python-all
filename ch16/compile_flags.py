import re

PHONE = re.compile(r"""
    (01[016789])    # 통신사 번호
    [-.\s]?         # 구분자는 있어도 없어도 된다
    (\d{3,4})       # 가운데 3~4자리
    [-.\s]?
    (\d{4})         # 끝 4자리
""", re.VERBOSE)

for text in ["010-1234-5678", "011.123.4567", "01012345678", "02-123-4567"]:
    m = PHONE.fullmatch(text)
    result = "-".join(m.groups()) if m else "휴대전화 번호가 아니다"
    print(text, "->", result)

print(re.findall(r"python", "Python PYTHON python", re.IGNORECASE))
