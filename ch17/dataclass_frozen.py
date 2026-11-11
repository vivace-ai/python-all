from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(3, 4)
visited = {p, Point(3, 4), Point(0, 0)}     # 집합에 넣을 수 있다
print(len(visited))

try:
    p.x = 10
except AttributeError as e:
    print(type(e).__name__, "-", e)
