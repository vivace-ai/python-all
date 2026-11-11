class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액이 부족하다")
        self.balance -= amount
        self.history.append(("출금", amount))   # 내역을 남긴다


# AI가 내놓은 코드: 한도까지 마이너스가 되는 계좌
class MinusAccount(Account):
    def __init__(self, owner, balance=0, limit=0):
        super().__init__(owner, balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount > self.balance + self.limit:
            raise ValueError("한도를 넘는다")
        self.balance -= amount


account = MinusAccount("이서연", 10000, limit=50000)
account.withdraw(30000)
print(account.balance, account.history)
