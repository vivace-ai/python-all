class Account:
    def __init__(self, balance):
        self.balance = balance


class SavingsAccount(Account):
    def add_interest(self, rate):
        self.balance += round(self.balance * rate)


account = Account(100000)
account.add_interest(0.02)
