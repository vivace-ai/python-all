# AI가 내놓은 코드: 금액 목록의 합계를 구한다
amounts = ["12000", "8500", "1,200", "3000원", "4500", "미정"]

total = 0
for text in amounts:
    try:
        total += int(text)
    except:
        pass
print("합계:", total)
