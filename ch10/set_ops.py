python_class = {"서연", "준호", "민지", "도윤"}
data_class = {"민지", "도윤", "하은"}

print(sorted(python_class | data_class))    # 합집합: 하나라도 듣는 사람
print(sorted(python_class & data_class))    # 교집합: 둘 다 듣는 사람
print(sorted(python_class - data_class))    # 차집합: 파이썬만 듣는 사람
print(sorted(python_class ^ data_class))    # 대칭차: 하나만 듣는 사람
print({"민지"} <= data_class)               # 부분집합인가
