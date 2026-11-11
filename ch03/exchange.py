# 입력
won = int(input("환전할 금액(원): "))
rate = float(input("환율(1달러당 원): "))

# 처리
dollar = won / rate

# 출력
print(f"{won:,}원 -> {dollar:,.2f}달러")
