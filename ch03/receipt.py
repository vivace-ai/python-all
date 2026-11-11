keyboard, mouse, monitor = 89000, 35000, 420000
total = keyboard * 2 + mouse + monitor

print(f"{'ITEM':<12}{'QTY':>4}{'PRICE':>12}")
print("-" * 28)
print(f"{'Keyboard':<12}{2:>4}{keyboard * 2:>12,}")
print(f"{'Mouse':<12}{1:>4}{mouse:>12,}")
print(f"{'Monitor':<12}{1:>4}{monitor:>12,}")
print("-" * 28)
print(f"{'TOTAL':<12}{4:>4}{total:>12,}")
