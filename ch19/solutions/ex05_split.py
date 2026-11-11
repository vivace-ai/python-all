def parse(line: str) -> tuple[str, int, int]:
    """'키보드,89000,2'를 (이름, 가격, 수량)으로 바꾼다."""
    name, price, count = line.split(",")
    return name, int(price), int(count)


def subtotal(items: list[tuple[str, int, int]]) -> int:
    """상품 금액의 합계를 구한다."""
    return sum(price * count for _, price, count in items)


def render(items: list[tuple[str, int, int]], total: int) -> str:
    """영수증 문자열을 만든다."""
    lines = [
        f"{name} x{count}  {price * count:,}원"
        for name, price, count in items
    ]
    lines.append(f"합계  {total:,}원")
    return "\n".join(lines)


items = [parse(line) for line in ["키보드,89000,1", "마우스,35000,2"]]
print(render(items, subtotal(items)))
