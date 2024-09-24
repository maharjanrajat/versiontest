# Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like circle, triangle, and square.

import math

# main shapes class
class Shape:
    def area(self):
        ...

    def perimeter(self):
        ...

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Subclass for Triangle 
class Triangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side

# Subclass for Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# main
circle = Circle(radius=5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

triangle = Triangle(side=3)
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())

square = Square(side=4)
print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())
