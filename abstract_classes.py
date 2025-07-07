# Polygon Calculator: Define an abstract base class Polygon with an abstract method area.
# Implement this in derived classes Rectangle and Triangle.


from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


rect = Rectangle(10, 20)
tri = Triangle(10, 10)
print("Rectangle Area:", rect.area())
print("Triangle Area:", tri.area())
