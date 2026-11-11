def to_won(amount):
    return f"{amount:,}원"


formatter = to_won    # 괄호 없이 쓰면 함수 자체를 가리킨다
print(formatter(15000))
