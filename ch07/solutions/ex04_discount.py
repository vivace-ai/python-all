def discounted(price, rate=0):
    """할인가를 원 단위로 돌려준다. 할인율이 0~1 밖이면 None."""
    if not 0 <= rate <= 1:
        return None
    return int(price * (1 - rate))


print(discounted(20000))
print(discounted(20000, 0.15))
print(discounted(20000, 1.5))
