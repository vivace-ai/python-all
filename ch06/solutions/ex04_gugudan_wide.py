for i in range(1, 10):          # 곱하는 수가 바깥쪽
    for dan in range(2, 10):    # 단이 안쪽
        print(f"{dan}x{i}={dan * i:>2}", end="  ")
    print()
