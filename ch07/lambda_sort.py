words = ["banana", "kiwi", "apple"]
print(sorted(words))                                # 사전 순서
print(sorted(words, key=len))                       # 길이가 짧은 순서

scores = [72, 95, 48, 61]
print(sorted(scores, key=lambda s: abs(s - 60)))    # 60점에 가까운 순서
