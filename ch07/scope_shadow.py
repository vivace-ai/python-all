count = 0


def increase():
    count = 10  # 전역 count와는 다른, 새 지역 변수다
    print("함수 안:", count)


increase()
print("함수 밖:", count)
