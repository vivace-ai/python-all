import numpy as np

scores = np.array([[80, 90, 70],
                   [65, 85, 95]])

print(scores.shape)         # (행의 수, 열의 수)
print(scores.mean(axis=1))  # 행마다의 평균
print(scores.mean(axis=0))  # 열마다의 평균
print(scores[:, 0])         # 모든 행의 0번 열
print(scores + 5)           # 2차원에서도 한꺼번에 계산된다
