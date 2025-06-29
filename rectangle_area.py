# Exercise 6: Design a Rectangle class with default attributes for length and width set to 1.
# Include methods to set these attributes and calculate the area.


class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width


    def set_length_and_width(self, new_length, new_width):
        self.length = new_length
        self.width = new_width

    def calculate_area(self):
        return self.length * self.width


def test_func():
    rect = Rectangle()
    assert rect.calculate_area() == 1

    rect.set_length_and_width(4, 5)
    assert rect.calculate_area() == 20