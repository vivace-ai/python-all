class EmailNotifier:
    def send(self, message):
        return f"[메일] {message}"


class SmsNotifier:
    def send(self, message):
        return f"[문자] {message[:10]}"     # 앞의 열 글자만 보낸다


class Recorder:
    """보내지 않고 받은 메시지를 기억만 한다. 시험할 때 쓴다."""

    def __init__(self):
        self.messages = []

    def send(self, message):
        self.messages.append(message)
        return "[기록]"


def notify_all(notifiers, message):
    return [notifier.send(message) for notifier in notifiers]


recorder = Recorder()
notifiers = [EmailNotifier(), SmsNotifier(), recorder]
print(notify_all(notifiers, "주문하신 상품이 출발했습니다"))
print(recorder.messages)
