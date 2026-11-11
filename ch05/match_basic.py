command = input("명령 (start/stop/status): ")

match command:
    case "start":
        print("작업을 시작합니다.")
    case "stop":
        print("작업을 멈춥니다.")
    case "status" | "info":     # 여러 값을 한 갈래로 묶는다
        print("작업이 진행 중입니다.")
    case _:                     # 어느 것에도 해당하지 않을 때
        print("알 수 없는 명령입니다.")
