from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def fee(self, amount):
        """결제 금액에 붙는 수수료."""

    def total(self, amount):
        return amount + self.fee(amount)


class CardPayment(Payment):
    def fee(self, amount):
        return round(amount * 0.02)


class TransferPayment(Payment):
    def fee(self, amount):
        return 500


for payment in (CardPayment(), TransferPayment()):
    print(type(payment).__name__, f"{payment.total(30000):,}원")

try:
    Payment()
except TypeError as e:
    print("만들 수 없다:", e)
