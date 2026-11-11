# longest_streak()가 지켜야 할 것을 먼저 적는다
from streak import longest_streak

assert longest_streak([]) == 0                  # 기록이 없다
assert longest_streak([3]) == 1                 # 하루뿐이다
assert longest_streak([1, 2, 3, 5, 6]) == 3     # 중간에 하루를 쉬었다
assert longest_streak([1, 1, 2, 2, 3]) == 3     # 하루에 기록이 여러 건이다
assert longest_streak([5, 1, 2]) == 2           # 순서가 섞여 있다
print("모든 확인을 통과했습니다.")
