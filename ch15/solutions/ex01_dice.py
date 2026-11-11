import random
from collections import Counter

random.seed(7)  # 같은 결과가 나오도록 난수의 출발점을 정한다

rolls = [random.randint(1, 6) for _ in range(600)]
counts = Counter(rolls)

for face in range(1, 7):
    print(f"{face}: {counts[face]}회")
print("가장 많이 나온 눈:", counts.most_common(1)[0][0])
