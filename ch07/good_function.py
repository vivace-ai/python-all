def monthly_payment(principal: int, months: int) -> int:
    """원금을 개월 수로 나눈 월 납입액을 원 단위로 돌려준다."""
    return principal // months


print(monthly_payment(1_200_000, 12))
print(monthly_payment.__doc__)
