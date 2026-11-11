def to_dollar(won, rate):
    return won / rate


def format_result(won, dollar):
    return f"{won:,}원 -> {dollar:,.2f}달러"


def main():
    won = int(input("환전할 금액(원): "))
    rate = float(input("환율(1달러당 원): "))
    print(format_result(won, to_dollar(won, rate)))


main()
