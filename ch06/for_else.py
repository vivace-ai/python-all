PASSWORD = "py2026"

for attempt in range(1, 4):     # 기회는 세 번
    typed = input(f"비밀번호 ({attempt}/3): ")
    if typed == PASSWORD:
        print("로그인되었습니다.")
        break
else:                           # break 없이 끝났을 때만 실행
    print("세 번 틀렸습니다. 계정을 잠급니다.")
