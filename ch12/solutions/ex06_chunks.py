def chunks(items, size):
    for start in range(0, len(items), size):
        yield items[start:start + size]     # size개씩 잘라 하나씩 내준다


for group in chunks(["서연", "준호", "민지", "도윤", "하은"], 2):
    print(group)
