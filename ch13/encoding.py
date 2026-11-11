text = "가계부"

print(text.encode("utf-8"))     # UTF-8: 한글 한 글자에 3바이트
print(text.encode("cp949"))     # CP949: 한글 한 글자에 2바이트

data = text.encode("utf-8")
print(data.decode("utf-8"))     # 같은 방식으로 풀면 원래 글자가 나온다
