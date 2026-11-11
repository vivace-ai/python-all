import re

pattern = r"\d{3}-\d{4}"

for text in ["010-1234", "전화 010-1234", "010-1234-5678"]:
    found = bool(re.search(pattern, text))          # 어디에든 있는가
    starts = bool(re.match(pattern, text))          # 처음부터 맞는가
    whole = bool(re.fullmatch(pattern, text))       # 전체가 맞는가
    print(f"{text:<14} search={found} match={starts} fullmatch={whole}")

for m in re.finditer(r"\d+", "3개 12개 150개"):     # Match 객체를 하나씩
    print(m.group(), m.span())
