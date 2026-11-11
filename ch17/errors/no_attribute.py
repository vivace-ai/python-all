class Account:
    def __init__(self, owner):
        self.owner = owner


account = Account("이서연")
print(account.balance)
