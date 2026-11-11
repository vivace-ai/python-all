score = 0
while score < 1 or score > 5:
    score = int(input("만족도를 1~5로 입력: "))
    if score < 1 or score > 5:
        print("1에서 5 사이의 숫자를 입력하세요.")

print(f"입력한 점수: {score}점")
