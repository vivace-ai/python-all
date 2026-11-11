import re


def is_phone(text):
    # 문자열 전체가 패턴과 맞아야 한다
    return bool(re.fullmatch(r"010-\d{4}-\d{4}", text))


for text in ["010-1234-5678", "010-1234-56789", "010-1234-5678 외 2건"]:
    print(f"{text:<22}", is_phone(text))
