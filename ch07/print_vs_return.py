def show_double(n):
    print(n * 2)    # 화면에 출력만 한다


def get_double(n):
    return n * 2    # 값을 호출한 곳으로 돌려준다


a = show_double(5)
b = get_double(5)
print(a, b)
