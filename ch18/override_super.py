from account import Account


class MinusAccount(Account):
    """정해진 한도까지 잔액이 0 아래로 내려갈 수 있는 계좌."""

    def __init__(self, owner, balance=0, limit=0):
        super().__init__(owner, balance)    # 부모의 초기화를 먼저 한다
        self.limit = limit                  # 자식에만 있는 속성

    def withdraw(self, amount):             # 부모의 메서드를 바꿔 쓴다
        if amount > self.balance + self.limit:
            raise ValueError("한도를 넘는다")
        self.balance -= amount

    def summary(self):                      # 부모의 결과에 덧붙인다
        return super().summary() + f" (한도 {self.limit:,}원)"


basic = Account("박준호", 10000)
minus = MinusAccount("이서연", 10000, limit=50000)

for account in (basic, minus):
    try:
        account.withdraw(30000)
    except ValueError as e:
        print(account.owner, "거절:", e)
    print(account.summary())
