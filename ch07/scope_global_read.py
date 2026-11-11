TAX_RATE = 0.1                          # 함수 밖에서 만든 이름: 전역 변수


def add_tax(price):
    return int(price * (1 + TAX_RATE))  # 함수 안에서 읽을 수 있다


print(add_tax(10000))
