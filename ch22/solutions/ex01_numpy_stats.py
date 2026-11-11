import numpy as np

temps = np.array([12.5, 15.0, 9.5, 17.0, 13.5, 8.0, 11.0])

print(temps.mean().round(1), temps.max(), temps.min())
print(temps.argmax())               # 가장 큰 값의 위치
print(temps[temps > temps.mean()])  # 평균보다 높은 값만
print(temps * 9 / 5 + 32)           # 화씨로 바꾼다
