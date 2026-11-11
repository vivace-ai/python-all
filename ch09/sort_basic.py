scores = [72, 95, 48, 61]

ordered = sorted(scores)    # 정렬한 새 리스트를 돌려준다
print(ordered, scores)

scores.sort(reverse=True)   # 리스트 자체를 큰 값부터 정렬한다
print(scores)

names = ["banana", "kiwi", "apple"]
names.sort(key=len)         # 길이를 기준으로
print(names)
