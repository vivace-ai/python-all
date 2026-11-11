def user_id(email):
    position = email.find("@")
    if position == -1:  # 찾지 못한 경우를 먼저 처리한다
        return None
    return email[:position]


print(user_id("seoyeon@example.com"))
print(user_id("seoyeon.example.com"))
