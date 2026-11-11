from collections import defaultdict

orders = [("서울", "키보드"), ("부산", "마우스"), ("서울", "모니터"),
          ("대구", "키보드"), ("부산", "키보드")]

by_city = defaultdict(list)
for city, item in orders:
    by_city[city].append(item)

for city in sorted(by_city):
    print(city, by_city[city])
