visits = ["home", "search", "home", "cart", "search", "pay"]

seen = set()    # 이미 본 값을 기억한다
unique = []     # 순서를 지키며 결과를 모은다
for page in visits:
    if page not in seen:
        seen.add(page)
        unique.append(page)

print(unique)
