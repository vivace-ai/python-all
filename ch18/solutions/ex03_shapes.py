class Shape:
    def area(self):
        raise NotImplementedError

    def __lt__(self, other):    # 넓이로 견준다
        return self.area() < other.area()

    def __repr__(self):
        return f"{type(self).__name__}({self.area():g})"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


shapes = [Square(3), Triangle(4, 3), Square(2)]
print(sorted(shapes))
print(max(shapes))
