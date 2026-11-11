def longest_streak(hours_list):
    """하루도 빠지지 않고 공부한 가장 긴 연속 일수를 돌려준다."""
    best = 0
    current = 0
    for hours in hours_list:
        if hours > 0:
            current += 1
        else:
            best = max(best, current)
            current = 0
    return max(best, current)   # 마지막 연속 구간도 견준다


print(longest_streak([1, 2, 0, 1, 1, 1]))
print(longest_streak([0, 0]))
print(longest_streak([2, 1, 1, 0, 3]))
