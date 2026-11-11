price1 = int(input("1번 품목 가격: "))
price2 = int(input("2번 품목 가격: "))
price3 = int(input("3번 품목 가격: "))

subtotal = price1 + price2 + price3
tax = int(subtotal * 0.1)

print("-" * 22)
print(f"{'SUBTOTAL':<10}{subtotal:>12,}")
print(f"{'TAX 10%':<10}{tax:>12,}")
print(f"{'TOTAL':<10}{subtotal + tax:>12,}")
