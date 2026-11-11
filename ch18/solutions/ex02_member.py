class Member:
    discount_rate = 0.0

    def __init__(self, name):
        self.name = name

    def price(self, amount):
        """할인을 적용한 결제 금액."""
        return round(amount * (1 - self.discount_rate))

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class SilverMember(Member):
    discount_rate = 0.05


class GoldMember(Member):
    discount_rate = 0.1


members = [Member("최민지"), SilverMember("박준호"), GoldMember("이서연")]
for member in members:
    print(member, f"{member.price(50000):,}원")
