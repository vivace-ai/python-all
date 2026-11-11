class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):          # print()와 str()이 부른다
        return f"{self.amount:,}원"

    def __repr__(self):         # 리스트 안이나 디버거에서 보이는 표기
        return f"Money({self.amount})"

    def __eq__(self, other):    # == 연산자가 부른다
        return self.amount == other.amount

    def __lt__(self, other):    # < 연산자가 부른다. 정렬에 쓰인다
        return self.amount < other.amount

    def __add__(self, other):   # + 연산자가 부른다
        return Money(self.amount + other.amount)


a = Money(3000)
b = Money(4500)
print(a)
print([a, b])
print(a == Money(3000), a == b)
print(a + b)
print(sorted([b, a]), max(a, b))
