values = ["12", "3.5", "", "abc", None]

for value in values:
    try:
        print(float(value))
    except (ValueError, TypeError) as e:    # 두 가지를 함께 잡는다
        print(f"{type(e).__name__}: {e}")
