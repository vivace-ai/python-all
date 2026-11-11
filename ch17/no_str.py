class Money:
    def __init__(self, amount):
        self.amount = amount


a = Money(3000)
print(a)                    # 무엇이 들었는지 알 수 없다
print(a == Money(3000))     # 값이 같아도 다르다고 한다
