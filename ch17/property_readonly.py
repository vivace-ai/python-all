class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance     # 밑줄: 밖에서 직접 건드리지 말라는 표시

    @property
    def balance(self):              # account.balance로 읽는다
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 한다")
        self._balance += amount


account = Account("이서연", 50000)
account.deposit(10000)
print(account.balance)              # 괄호 없이 읽는다

try:
    account.balance = -1            # 대입은 막혀 있다
except AttributeError as e:
    print("거절:", e)
