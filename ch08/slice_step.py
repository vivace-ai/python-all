text = "ABCDEFGH"

print(text[::2])    # 두 칸씩 건너뛴다
print(text[1::2])
print(text[::-1])   # 간격이 -1이면 거꾸로
print(text[2:100])  # 범위를 넘어도 오류가 나지 않는다
