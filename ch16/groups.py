import re

m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "마감은 2026-11-30입니다.")
print(m.group())                # 0번: 패턴 전체에 맞은 부분
print(m.group(1), m.group(2))   # 괄호 번호로 꺼낸다
year, month, day = m.groups()   # 모든 그룹을 튜플로
print(int(month), int(day))

# 그룹에 이름을 붙인다
m = re.search(r"(?P<user>[\w.]+)@(?P<domain>[\w.]+)", "help@example.com")
print(m.group("user"), m.group("domain"))
print(m.groupdict())

# findall은 그룹이 여럿이면 튜플을 담는다
print(re.findall(r"(\w+)=(\d+)", "width=640 height=480"))

# (?: )는 묶기만 하고 그룹으로 세지 않는다
print(re.findall(r"\d+(?:px|em)", "12px 3em 40pt"))
