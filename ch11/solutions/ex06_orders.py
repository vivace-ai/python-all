orders = [
    {"customer": "이서연", "amount": 42000},
    {"customer": "박준호", "amount": 18000},
    {"customer": "이서연", "amount": 27000},
    {"customer": "최민지", "amount": 65000},
    {"customer": "박준호", "amount": 9000},
]

totals = {}
for order in orders:
    name = order["customer"]
    totals[name] = totals.get(name, 0) + order["amount"]

ranked = sorted(totals.items(), key=lambda item: item[1], reverse=True)
for rank, (name, amount) in enumerate(ranked, start=1):
    print(f"{rank}위 {name} {amount:>8,}원")
