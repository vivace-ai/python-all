# lines.py가 만든 records.txt를 읽는다
with open("records.txt", encoding="utf-8") as f:
    print(f.readlines())            # 줄바꿈이 붙은 줄의 리스트

with open("records.txt", encoding="utf-8") as f:
    print(f.read().splitlines())    # 줄바꿈을 뗀 줄의 리스트

with open("records.txt", encoding="utf-8") as f:
    print(repr(f.readline()))       # 한 줄만 읽는다
    rest = f.read()                 # 읽던 자리부터 끝까지 읽는다
    print(len(rest.splitlines()))
    print(repr(f.read()))           # 끝까지 읽은 뒤에는 빈 문자열이다
