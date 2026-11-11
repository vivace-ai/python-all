import re


class SignupError(Exception):
    """가입 정보가 잘못되었다."""


class InvalidEmailError(SignupError):
    pass


class WeakPasswordError(SignupError):
    def __init__(self, reason):
        super().__init__(f"비밀번호가 약하다: {reason}")
        self.reason = reason


def signup(email, password):
    if not re.fullmatch(r"[\w.]+@[\w.]+\.\w+", email):
        raise InvalidEmailError(f"이메일 형식이 아니다: {email}")
    if len(password) < 8:
        raise WeakPasswordError("8자 이상이어야 한다")
    if not re.search(r"\d", password):
        raise WeakPasswordError("숫자가 있어야 한다")
    return f"{email} 가입 완료"


for email, password in [("kim@example.com", "python2026"),
                        ("kim.example.com", "python2026"),
                        ("lee@example.com", "python")]:
    try:
        print(signup(email, password))
    except SignupError as e:
        print(type(e).__name__, "-", e)
