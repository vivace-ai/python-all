import re

text = "문의는 02-123-4567 또는 010-1234-5678로 주세요."

print("010" in text)                        # 정해진 글자는 in으로 찾는다

m = re.search(r"\d{3}-\d{4}-\d{4}", text)   # 무늬는 정규표현식으로 찾는다
print(m)
print(m.group())                            # 찾은 문자열
print(m.start(), m.end())                   # 찾은 위치

print(re.search(r"\d{5}", text))            # 없으면 None
