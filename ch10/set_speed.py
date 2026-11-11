import time

numbers_list = list(range(100_000))
numbers_set = set(numbers_list)
targets = range(99_500, 100_000)    # 뒤쪽에 있는 값 500개를 찾는다

start = time.perf_counter()
for target in targets:
    target in numbers_list
list_time = time.perf_counter() - start

start = time.perf_counter()
for target in targets:
    target in numbers_set
set_time = time.perf_counter() - start

print(f"리스트: {list_time:.6f}초")
print(f"집합:   {set_time:.6f}초")
