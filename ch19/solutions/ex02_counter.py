def make_counter():
    count = 0

    def increase():
        nonlocal count  # 바깥 함수의 변수를 바꾸겠다는 선언
        count += 1
        return count

    return increase


visits = make_counter()
clicks = make_counter()
print(visits(), visits(), visits())
print(clicks())         # 카운터마다 따로 센다
