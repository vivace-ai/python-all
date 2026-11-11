class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.history = []   # (종류, 금액) 튜플을 차례로 담는다

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("입금", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액이 부족하다")
        self.balance -= amount
        self.history.append(("출금", amount))

    def print_history(self):
        for kind, amount in self.history:
            print(f"{kind} {amount:>8,}원")
        print(f"잔액 {self.balance:>8,}원")


account = Account("이서연")
account.deposit(50000)
account.withdraw(12000)
account.deposit(3000)
account.print_history()
