for i in range(1, 10):          # 곱하는 수
    for dan in range(2, 6):     # 2단부터 5단
        print(f"{dan} x {i} = {dan * i:>2}", end="   ")
    print()                     # 한 줄을 마치고 줄바꿈
