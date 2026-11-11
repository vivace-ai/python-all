text = "the quick brown fox jumps over the lazy dog"

print(text.find("quick"))   # 처음 나타나는 위치
print(text.find("cat"))     # 없으면 -1
print(text.count("the"))    # 나타나는 횟수
print(text.startswith("the"), text.endswith("dog"))
print("fox" in text)        # 있는지만 확인할 때는 in
