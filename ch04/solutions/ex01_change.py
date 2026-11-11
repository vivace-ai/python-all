price = int(input("물건값: "))
paid = int(input("낸 돈: "))

change = paid - price
print(f"거스름돈: {change:,}원")

print(f"10000원: {change // 10000}장")
change %= 10000     # 만 원권을 떼고 남은 돈
print(f" 1000원: {change // 1000}장")
change %= 1000
print(f"  100원: {change // 100}개")
