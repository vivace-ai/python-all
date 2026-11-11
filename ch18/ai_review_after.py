class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def available(self):
        """지금 출금할 수 있는 최대 금액."""
        return self.balance

    def withdraw(self, amount):
        if amount > self.available():   # 자식이 바꿀 수 있는 부분
            raise ValueError("출금할 수 있는 금액을 넘는다")
        self.balance -= amount
        self.history.append(("출금", amount))


class MinusAccount(Account):
    def __init__(self, owner, balance=0, limit=0):
        super().__init__(owner, balance)
        self.limit = limit

    def available(self):                # 달라지는 것만 재정의한다
        return self.balance + self.limit


account = MinusAccount("이서연", 10000, limit=50000)
account.withdraw(30000)
print(account.balance, account.history)
