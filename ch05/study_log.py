# 학습 기록 프로그램 1단계: 하루 학습 시간을 받아 한 줄 평을 출력한다
hours = float(input("오늘 학습 시간: "))

if hours < 0 or hours > 24:
    print("0에서 24 사이로 입력하세요.")
elif hours == 0:
    print("오늘은 쉬어 가는 날입니다.")
elif hours < 1:
    print("짧게라도 이어 간 것이 중요합니다.")
elif hours < 3:
    print("꾸준한 속도입니다.")
else:
    print("집중한 하루였습니다.")
