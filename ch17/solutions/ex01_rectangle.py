class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{self.width}x{self.height} 직사각형"


r = Rectangle(4, 3)
print(r)
print("넓이:", r.area())
print("둘레:", r.perimeter())
