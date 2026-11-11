def parse(text):
    return float(text)          # 예외는 여기서 난다


def total(texts):
    result = 0
    for text in texts:
        result += parse(text)
    return result


def main():
    try:
        print(total(["1.5", "2", "세 시간"]))
    except ValueError as e:     # 두 단계 위에서 잡는다
        print("숫자가 아닌 값이 있습니다:", e)


main()
