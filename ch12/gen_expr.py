import sys

squares_list = [n * n for n in range(100_000)]  # 대괄호: 리스트
squares_gen = (n * n for n in range(100_000))   # 소괄호: 제너레이터

print(sys.getsizeof(squares_list))              # 차지하는 메모리(바이트)
print(sys.getsizeof(squares_gen))
print(sum(squares_gen))                         # 값을 하나씩 받아 더한다

scores = [72, 95, 48, 61]
print(any(s >= 90 for s in scores))             # 하나라도 참인가
print(all(s >= 60 for s in scores))             # 모두 참인가
