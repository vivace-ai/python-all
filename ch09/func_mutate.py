def add_bonus(scores):
    for i in range(len(scores)):
        scores[i] += 5          # 넘겨받은 리스트를 직접 고친다


def with_bonus(scores):
    result = []
    for score in scores:
        result.append(score + 5)
    return result               # 새 리스트를 돌려준다


data = [72, 95]
add_bonus(data)
print(data)                     # 원본이 바뀌었다

data = [72, 95]
print(with_bonus(data), data)   # 원본은 그대로다
