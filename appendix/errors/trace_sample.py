def parse_hours(text):
    return float(text)


def total_hours(entries):
    total = 0
    for entry in entries:
        total += parse_hours(entry)
    return total


print(total_hours(["1.5", "2", "한 시간"]))
