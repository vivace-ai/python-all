# AI가 내놓은 코드: 휴대전화 번호 형식인지 검사한다
import re


def is_phone(text):
    return bool(re.match(r"010-\d{4}-\d{4}", text))


for text in ["010-1234-5678", "010-1234-56789", "010-1234-5678 외 2건"]:
    print(f"{text:<22}", is_phone(text))
