items = ["노트북", "모니터", "키보드"]
prices = [1_350_000, 420_000, 89_000]

for item, price in zip(items, prices):
    print(f"{item:<4} {price:>10,}원")
