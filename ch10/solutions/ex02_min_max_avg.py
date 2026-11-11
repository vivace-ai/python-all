def analyze(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


low, high, avg = analyze([12000, 8500, 23000, 15000])
print(f"최저 {low:,}원, 최고 {high:,}원, 평균 {avg:,.0f}원")
