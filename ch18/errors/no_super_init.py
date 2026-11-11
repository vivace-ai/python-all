class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


class MinusAccount(Account):
    def __init__(self, owner, limit):
        self.limit = limit


account = MinusAccount("이서연", 50000)
print(account.balance)
