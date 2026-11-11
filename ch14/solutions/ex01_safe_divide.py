def safe_divide(a, b):
    """a를 b로 나눈 값을 돌려준다. 나눌 수 없으면 None."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


print(safe_divide(10, 4))
print(safe_divide(10, 0))
