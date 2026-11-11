import re

m = re.search(r"(\d+)원", "합계 4500원")
print(m.group(2))
