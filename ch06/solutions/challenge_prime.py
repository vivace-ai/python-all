n = int(input("정수를 입력: "))

if n < 2:
    print(f"{n}: 소수가 아닙니다.")
else:
    divisor = 2
    while divisor * divisor <= n:   # 제곱근까지만 확인하면 충분하다
        if n % divisor == 0:
            print(f"{n}: 소수가 아닙니다. ({divisor}로 나누어떨어짐)")
            break
        divisor += 1
    else:
        print(f"{n}: 소수입니다.")
