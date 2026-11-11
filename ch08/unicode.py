print(len("Python"), len("파이썬"))     # len()은 글자 수를 센다
print(ord("A"), ord("가"))              # 글자에 매겨진 번호
print(chr(65), chr(44032))              # 번호에 해당하는 글자

data = "파이썬".encode("utf-8")         # 저장하고 전송할 때의 모습
print(data)
print(len(data))                        # 한글 한 글자는 UTF-8에서 3바이트
