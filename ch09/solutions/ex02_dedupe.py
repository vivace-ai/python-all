def dedupe(items):
    result = []
    for item in items:
        if item not in result:  # 처음 보는 값만 담는다
            result.append(item)
    return result


print(dedupe(["회의", "메일", "회의", "보고서", "메일"]))
