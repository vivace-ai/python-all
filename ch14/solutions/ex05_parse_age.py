def parse_age(text):
    """문자열을 나이로 바꾼다. 쓸 수 없는 값이면 까닭을 담아 ValueError."""
    try:
        age = int(text)
    except ValueError:
        raise ValueError(f"정수가 아니다: {text}")
    if not 0 <= age <= 130:
        raise ValueError(f"범위를 벗어났다: {age}")
    return age


for text in ["34", "서른넷", "-5", "200"]:
    try:
        print(parse_age(text))
    except ValueError as e:
        print("거절 -", e)
