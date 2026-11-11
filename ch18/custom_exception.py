class OrderError(Exception):
    """주문 처리에서 생기는 모든 오류의 부모."""


class InvalidQuantityError(OrderError):
    """수량이 잘못되었다."""


class OutOfStockError(OrderError):
    """재고가 모자란다."""

    def __init__(self, item, left):
        super().__init__(f"{item}의 재고가 {left}개뿐이다")
        self.item = item        # 잡는 쪽에서 쓸 정보를 담아 둔다
        self.left = left


def order(stock, item, count):
    if count <= 0:
        raise InvalidQuantityError(f"수량이 잘못되었다: {count}")
    left = stock.get(item, 0)
    if left < count:
        raise OutOfStockError(item, left)
    stock[item] = left - count


stock = {"키보드": 2}
for item, count in [("키보드", 1), ("키보드", 5), ("마우스", 0)]:
    try:
        order(stock, item, count)
        print(f"{item} {count}개 주문 완료")
    except OutOfStockError as e:
        print(f"재고 부족: {e.item}는 {e.left}개까지 주문할 수 있습니다.")
    except OrderError as e:     # 나머지 주문 오류를 한꺼번에 잡는다
        print("주문 오류:", e)
