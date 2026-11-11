"""가격 계산을 맡는다."""

FREE_SHIPPING_FROM = 50000
SHIPPING_FEE = 3000


def shipping_fee(subtotal):
    """상품 금액에 따른 배송비를 돌려준다."""
    return 0 if subtotal >= FREE_SHIPPING_FROM else SHIPPING_FEE
