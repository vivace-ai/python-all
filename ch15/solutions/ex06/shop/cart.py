"""장바구니 계산을 맡는다."""
from .pricing import shipping_fee


def subtotal(items):
    """(이름, 가격, 수량) 튜플의 리스트에서 상품 금액을 구한다."""
    return sum(price * count for _, price, count in items)


def total(items):
    """상품 금액에 배송비를 더한 결제 금액을 구한다."""
    amount = subtotal(items)
    return amount + shipping_fee(amount)
