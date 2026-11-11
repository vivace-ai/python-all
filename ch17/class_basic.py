class Account:
    """예금 계좌."""

    def __init__(self, owner, balance):
        self.owner = owner      # 객체마다 따로 가지는 값
        self.balance = balance


a = Account("이서연", 50000)    # 클래스를 호출하면 객체가 만들어진다
b = Account("박준호", 12000)

print(a.owner, a.balance)
print(b.owner, b.balance)

a.balance += 10000              # a의 잔액만 바뀐다
print(a.balance, b.balance)
print(type(a).__name__, isinstance(a, Account))
