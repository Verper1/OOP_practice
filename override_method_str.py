# Person Class with __str__ Method: Create a Person class with first and last name attributes and override
# the __str__ method to return the full name.


class Person:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    def __str__(self):
        return f"Имя: {self.first_name} Фамилия: {self.second_name}"


def test_func():
    p1 = Person("Олег", "Бруно")
    assert p1.__str__() == f"Имя: {p1.first_name} Фамилия: {p1.second_name}"