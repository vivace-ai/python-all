from typing import Protocol


class Notifier(Protocol):
    """send()가 있는 객체라면 무엇이든 Notifier다."""

    def send(self, message: str) -> None: ...


class ConsoleNotifier:  # Notifier를 물려받지 않았다
    def send(self, message: str) -> None:
        print("[알림]", message)


def notify(notifier: Notifier, message: str) -> None:
    notifier.send(message)


notify(ConsoleNotifier(), "배송이 시작되었습니다.")
