point = (3, 4)              # 소괄호로 묶으면 튜플이다

print(point[0], point[1])   # 꺼내는 법은 리스트와 같다
print(len(point))

rgb = 255, 128, 0           # 괄호를 생략해도 쉼표가 튜플을 만든다
print(rgb)

single = (5,)               # 항목이 하나면 쉼표를 붙인다
print(type(single), type((5)))
