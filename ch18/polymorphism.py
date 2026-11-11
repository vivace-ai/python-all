import math


class Shape:
    """모든 도형의 부모."""

    name = "도형"

    def area(self):
        raise NotImplementedError("자식 클래스가 정의해야 한다")

    def describe(self):
        # self.area()는 그 객체의 클래스에 정의된 area()다
        return f"{self.name}: 넓이 {self.area():.1f}"


class Rectangle(Shape):
    name = "직사각형"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    name = "원"

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


shapes = [Rectangle(4, 3), Circle(1), Rectangle(2, 2)]
for shape in shapes:
    print(shape.describe())     # 어떤 도형인지 묻지 않는다
print(f"합계: {sum(shape.area() for shape in shapes):.1f}")
