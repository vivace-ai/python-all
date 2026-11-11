prices = [12000, 8500, 23000]
for price in prices:
    tax = price // 10   # 부가세 10%
    print(f"{price:>6}원  부가세 {tax:>5}원")
print("계산 완료")      # 반복이 끝난 뒤 한 번만 실행
