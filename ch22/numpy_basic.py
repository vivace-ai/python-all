import numpy as np

hours = [1.5, 2.0, 0.5, 1.0]
print([h * 60 for h in hours])  # 리스트: 항목마다 계산하려면 반복이 필요하다

arr = np.array(hours)
print(arr * 60)                 # 배열: 모든 항목에 한꺼번에 계산된다
print(arr.shape, arr.dtype)
print(arr.sum(), arr.mean(), arr.max())

print(arr > 1.0)                # 조건을 걸면 참과 거짓의 배열이 나온다
print(arr[arr > 1.0])           # 그 배열로 항목을 고른다
