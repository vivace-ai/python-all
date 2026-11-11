def summarize(scores):
    return min(scores), max(scores), sum(scores) / len(scores)


result = summarize([72, 95, 48, 61])
print(result)                       # 돌려준 것은 튜플 하나다

lowest, highest, average = result   # 받는 쪽에서 풀어 담는다
print(lowest, highest, average)
