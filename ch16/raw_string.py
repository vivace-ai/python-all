import re

# r을 붙이면 역슬래시가 글자 그대로 남는다
print(len("\n"), len(r"\n"))
print(len("\b"), len(r"\b"))

print(re.search("\bcat\b", "a cat"))    # r이 없다: 찾지 못한다
print(re.search(r"\bcat\b", "a cat"))   # r이 있다: 찾는다
