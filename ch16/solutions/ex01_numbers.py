import re

text = "사과 3개, 배 12개, 감 150개를 주문했다."

numbers = [int(n) for n in re.findall(r"\d+", text)]
print(numbers)
print("합계:", sum(numbers))
