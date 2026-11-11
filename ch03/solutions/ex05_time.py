seconds = int(input("초: "))

hours = seconds // 3600         # 3600초가 몇 번 들어가는가
minutes = seconds % 3600 // 60  # 남은 초에서 분을 구한다
rest = seconds % 60

print(f"{hours:02d}:{minutes:02d}:{rest:02d}")
