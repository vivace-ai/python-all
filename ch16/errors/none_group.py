import re

m = re.search(r"\d{3}-\d{4}", "전화번호 없음")
print(m.group())
