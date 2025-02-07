import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Точка: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

point1 = Point(3, 4)
point1.show()

point1.move(2, -1)
point1.show()

point2 = Point(6, 8)
print(f"Расстояние между точками: {point1.dist(point2)}")
