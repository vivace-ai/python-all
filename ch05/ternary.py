age = 17
label = "성인" if age >= 19 else "미성년"
print(label)

total = 62000
shipping = 0 if total >= 50000 else 3000
print(f"배송비: {shipping:,}원")
