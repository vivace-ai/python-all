def old(hours: float) -> str:
    total = round(hours * 60)
    h, m = divmod(total, 60)
    return f"{h}시간 {m}분"


def new(hours: float) -> str:
    h = int(hours)
    m = int((hours - h) * 60)
    return f"{h}시간 {m}분"


# 0.0부터 5.0까지 0.05시간 간격으로 두 함수의 결과를 견준다
inputs = [n / 20 for n in range(101)]
changed = [x for x in inputs if old(x) != new(x)]

print(f"{len(inputs)}개 가운데 {len(changed)}개의 결과가 다르다")
for x in changed[:3]:
    print(x, "|", old(x), "|", new(x))
