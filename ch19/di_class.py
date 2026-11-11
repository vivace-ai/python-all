class ConsoleNotifier:
    def send(self, message):
        print("[알림]", message)


class FakeNotifier:
    """보내는 척만 하고 메시지를 모아 둔다. 시험할 때 쓴다."""

    def __init__(self):
        self.sent = []

    def send(self, message):
        self.sent.append(message)


class OrderService:
    def __init__(self, notifier):
        self.notifier = notifier    # 알림을 보낼 객체를 건네받는다

    def place(self, item):
        self.notifier.send(f"{item} 주문이 접수되었습니다.")


OrderService(ConsoleNotifier()).place("키보드")

fake = FakeNotifier()
OrderService(fake).place("마우스")
print(fake.sent)
