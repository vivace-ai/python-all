"""이 장의 예제가 함께 쓰는 기본 계좌 클래스."""


class Account:
    """예금 계좌."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액이 부족하다")
        self.balance -= amount

    def summary(self):
        return f"{self.owner}: {self.balance:,}원"
