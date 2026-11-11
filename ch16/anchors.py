import re

lines = ["ERROR 디스크 부족", "INFO 시작", "이전 ERROR 무시"]

# ^는 처음, $는 끝
print([line for line in lines if re.search(r"^ERROR", line)])
print([line for line in lines if re.search(r"무시$", line)])

print(re.findall(r"cat", "cat concat cats"))        # 낱말 속의 cat도 잡힌다
print(re.findall(r"\bcat\b", "cat concat cats"))    # 낱말 cat만 잡힌다
print(re.findall(r"colou?r", "color colour"))       # u가 있어도 없어도
print(re.findall(r"a{2,3}", "a aa aaa aaaa"))       # a가 2~3번
