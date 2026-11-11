age = int(input("나이: "))

if age < 0:
    print("나이를 다시 확인하세요.")
elif age < 8:
    print("입장료: 무료")
elif age < 19:
    print("입장료: 5,000원")
elif age < 65:
    print("입장료: 10,000원")
else:
    print("입장료: 3,000원")
