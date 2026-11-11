import random

secret = random.randint(1, 100)
print("1부터 100 사이의 숫자를 맞혀 보세요. 기회는 7번입니다.")

for attempt in range(1, 8):
    guess = int(input(f"{attempt}번째 추측 > "))
    if guess < secret:
        print("더 큰 수입니다.")
    elif guess > secret:
        print("더 작은 수입니다.")
    else:
        print(f"정답입니다. {attempt}번 만에 맞혔습니다.")
        break
else:
    print(f"기회를 모두 썼습니다. 정답은 {secret}입니다.")
