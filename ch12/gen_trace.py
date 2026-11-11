def steps():
    print("  [제너레이터] 시작")
    yield 1
    print("  [제너레이터] 이어서 실행")
    yield 2
    print("  [제너레이터] 끝")


for value in steps():
    print("받은 값:", value)
