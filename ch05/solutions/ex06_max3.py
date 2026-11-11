a = int(input("첫 번째 수: "))
b = int(input("두 번째 수: "))
c = int(input("세 번째 수: "))

largest = a     # 일단 첫 번째 수를 가장 큰 수로 둔다
if b > largest:
    largest = b
if c > largest:
    largest = c

print(f"가장 큰 수: {largest}")
