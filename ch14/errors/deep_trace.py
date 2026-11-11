def parse(text):
    return float(text)


def total(texts):
    result = 0
    for text in texts:
        result += parse(text)
    return result


print(total(["1.5", "세 시간"]))
