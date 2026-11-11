def to_numbers(texts):
    """숫자로 바뀐 값의 리스트와 바꾸지 못한 값의 리스트를 돌려준다."""
    numbers = []
    failed = []
    for text in texts:
        try:
            numbers.append(float(text))
        except ValueError:
            failed.append(text)
    return numbers, failed


numbers, failed = to_numbers(["3", "4.5", "다섯", "6", "-"])
print("변환:", numbers)
print("실패:", failed)
