class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @classmethod
    def from_text(cls, text):
        """'이서연,50000' 모양의 문자열로 계좌를 만든다."""
        owner, balance = text.split(",")
        return cls(owner, int(balance))     # cls는 Account 자신이다


account = Account.from_text("이서연,50000")
print(account.owner, account.balance)
