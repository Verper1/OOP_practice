# Polymorphism with a Function: Create a function describe_pet that takes an object of Animal and calls
# its speak method, demonstrating polymorphism.
import pytest


class Animal:
    def speak(self):
        print("NotImplementedError(\"Subclasses must implement this method\")")
        raise NotImplementedError("Subclasses must implement this method")


class Cat(Animal):
    def speak(self):
        print('Метод speak Cat')
        return 'Метод speak Cat'


class Dog(Animal):
    def speak(self):
        print('Метод speak Dog')
        return 'Метод speak Dog'


def speak(animal):
    return animal.speak()


def test_func():
    c1 = Cat()
    d1 = Dog()
    a1 = Animal()

    assert speak(c1) == "Метод speak Cat"
    assert speak(d1) == "Метод speak Dog"
    with pytest.raises(NotImplementedError) as exc_info:  # Чтобы тест проверял, что вызов метода speak(a1) действительно вызывает исключение NotImplementedError с указанным сообщением, нужно использовать pytest.raises в контекстном менеджере
        a1.speak()
    assert str(exc_info.value) == "Subclasses must implement this method"
