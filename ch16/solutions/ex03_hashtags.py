import re

post = "오늘도 #파이썬 공부 완료. #python3 #100일_챌린지 37일차"

print(re.findall(r"#(\w+)", post))  # 괄호 안만 결과에 담긴다
