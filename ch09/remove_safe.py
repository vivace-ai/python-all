numbers = [1, 2, 2, 3]

kept = []
for n in numbers:
    if n != 2:
        kept.append(n)  # 남길 값만 새 리스트에 모은다

print(kept)
