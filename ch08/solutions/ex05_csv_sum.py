line = "12000, 8500, 23000"

total = 0
for part in line.split(","):
    total += int(part.strip())  # 조각마다 공백을 없애고 정수로 바꾼다

print(f"합계: {total:,}원")
