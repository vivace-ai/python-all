numbers = range(1_000_000)

print(numbers)              # 숫자 백만 개가 아니라 '규칙'이 출력된다
print(len(numbers))
print(999_999 in numbers)   # 포함 여부는 계산으로 바로 답한다
print(list(range(5)))       # 값이 필요하면 list()로 펼친다
