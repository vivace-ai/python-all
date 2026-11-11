print("12345".isdigit())                    # 숫자로만 이루어졌는가
print("12.5".isdigit(), "-3".isdigit())     # 소수점과 부호는 숫자가 아니다
print("Python".isalpha(), "Python3".isalnum())
print("   ".strip() == "")                  # 공백뿐인 입력인가
