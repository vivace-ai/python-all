import re


def with_tax(m):
    """찾은 금액에 부가세 10%를 더한 문자열을 돌려준다."""
    price = int(m.group(1))
    return f"{round(price * 1.1):,}원"


print(re.sub(r"(\d+)원", with_tax, "커피 4500원, 케이크 6000원"))
