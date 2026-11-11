class Account:
    bank = "파이은행"       # 클래스 속성: 모든 객체가 함께 본다
    count = 0

    def __init__(self, owner):
        self.owner = owner  # 인스턴스 속성: 객체마다 따로 가진다
        Account.count += 1


a = Account("이서연")
b = Account("박준호")
print(a.bank, b.bank, Account.bank)
print(Account.count)

a.bank = "다른은행"         # a에만 인스턴스 속성이 새로 생긴다
print(a.bank, b.bank, Account.bank)
