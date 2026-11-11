from account import Account


class SavingsAccount(Account):  # Account를 물려받는다
    """이자가 붙는 저축 계좌."""

    def add_interest(self, rate):
        self.balance += round(self.balance * rate)


savings = SavingsAccount("이서연", 100000)
savings.deposit(50000)          # 물려받은 메서드
savings.add_interest(0.02)      # 새로 더한 메서드
print(savings.summary())

print(isinstance(savings, SavingsAccount), isinstance(savings, Account))
print(issubclass(SavingsAccount, Account))
