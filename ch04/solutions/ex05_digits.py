number = int(input("세 자리 수: "))

hundreds = number // 100
tens = number // 10 % 10
ones = number % 10

print(f"{hundreds} + {tens} + {ones} = {hundreds + tens + ones}")
