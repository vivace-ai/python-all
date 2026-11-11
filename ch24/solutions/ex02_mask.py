def mask_email(email: str) -> str:
    """전자우편 주소의 @ 앞을 첫 글자만 남기고 *로 가린다."""
    name, _, domain = email.partition("@")
    if not name or not domain:
        raise ValueError(f"전자우편 주소가 아니다: {email}")
    return name[0] + "*" * (len(name) - 1) + "@" + domain


# 함수를 쓰기 전에 먼저 적은 확인
assert mask_email("kim@example.com") == "k**@example.com"
assert mask_email("a@example.com") == "a@example.com"
assert mask_email("python@vivace.ai") == "p*****@vivace.ai"
try:
    mask_email("주소가 아님")
except ValueError:
    pass
else:
    raise AssertionError("@가 없으면 ValueError가 나야 한다")

print(mask_email("kim@example.com"))
print("모든 확인을 통과했습니다.")
