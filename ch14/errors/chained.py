def load_price(text):
    try:
        return int(text)
    except ValueError as e:
        raise ValueError(f"가격 형식이 틀렸다: {text}") from e


load_price("1,200원")
