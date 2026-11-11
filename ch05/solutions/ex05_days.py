month = int(input("월: "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"{month}월은 31일까지 있습니다.")
    case 4 | 6 | 9 | 11:
        print(f"{month}월은 30일까지 있습니다.")
    case 2:
        print("2월은 28일까지 있습니다. 윤년에는 29일입니다.")
    case _:
        print("1에서 12 사이의 값을 입력하세요.")
