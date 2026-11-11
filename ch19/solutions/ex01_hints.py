def count_long_words(text: str, minimum: int = 5) -> int:
    """minimum 글자 이상인 낱말의 수를 돌려준다."""
    return len([word for word in text.split() if len(word) >= minimum])


def find_price(prices: dict[str, int], name: str) -> int | None:
    """상품의 가격을 돌려준다. 없는 상품이면 None."""
    return prices.get(name)


print(count_long_words("python makes data analysis simple"))
print(find_price({"키보드": 89000}, "키보드"), find_price({}, "마우스"))
