age = 5
is_member = False

print(age < 8 or age >= 65 and is_member)       # and가 or보다 먼저다
print((age < 8 or age >= 65) and is_member)     # 괄호로 순서를 바꿨다
