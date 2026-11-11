import re

html = "<b>굵게</b>와 <i>기울임</i>"

print(re.findall(r"<.+>", html))        # 탐욕: 갈 수 있는 데까지 간다
print(re.findall(r"<.+?>", html))       # 게으름: 맞는 순간 멈춘다
print(re.findall(r"<[^>]+>", html))     # 범위를 좁힌다: > 가 아닌 글자만
