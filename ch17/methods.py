class Account:
    """예금 계좌."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """입금한다."""
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 한다")
        self.balance += amount

    def withdraw(self, amount):
        """출금한다. 잔액이 모자라면 거절한다."""
        if amount > self.balance:
            raise ValueError("잔액이 부족하다")
        self.balance -= amount

    def summary(self):
        return f"{self.owner}: {self.balance:,}원"


account = Account("이서연")
account.deposit(50000)
account.withdraw(12000)
print(account.summary())
print(Account.summary(account))     # 바로 윗줄과 같은 호출이다

try:
    account.withdraw(100000)
except ValueError as e:
    print("거절:", e)
