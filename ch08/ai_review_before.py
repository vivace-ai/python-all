# AI가 내놓은 코드: 이메일 주소에서 아이디를 꺼낸다
def user_id(email):
    return email[:email.find("@")]


print(user_id("seoyeon@example.com"))
print(user_id("seoyeon.example.com"))   # @를 빠뜨린 잘못된 주소
