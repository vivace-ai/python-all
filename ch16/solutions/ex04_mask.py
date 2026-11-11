import re

text = "담당: kim.younghee@example.com, 참조: lee@example.co.kr"

print(re.sub(r"(\w)[\w.]*@", r"\1***@", text))  # 첫 글자만 남긴다
