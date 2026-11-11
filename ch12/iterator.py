numbers = [10, 20, 30]

it = iter(numbers)      # 리스트에서 이터레이터를 얻는다
print(next(it))         # 다음 값을 하나 꺼낸다
print(next(it))
print(next(it))
print(next(it, "끝"))   # 더 없을 때 돌려줄 값을 정할 수 있다
