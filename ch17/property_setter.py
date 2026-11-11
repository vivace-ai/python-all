class Session:
    """한 번의 학습."""

    def __init__(self, subject, hours):
        self.subject = subject
        self.hours = hours      # 아래의 setter를 거친다

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):     # session.hours = 값 으로 대입할 때 불린다
        if not 0 <= value <= 24:
            raise ValueError(f"시간은 0에서 24 사이여야 한다: {value}")
        self._hours = value


session = Session("파이썬", 1.5)
session.hours = 2               # 검사를 통과한다
print(session.hours)

try:
    session.hours = 30
except ValueError as e:
    print("거절:", e)
