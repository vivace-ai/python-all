def rectangle_area(width, height):
    return width * height


print(rectangle_area(3, 4))                 # 위치 인자: 순서대로 넘긴다
print(rectangle_area(height=4, width=3))    # 키워드 인자: 이름으로 넘긴다
