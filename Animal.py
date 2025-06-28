# Создайте базовый класс Animal с методом speak. Затем создайте два подкласса Dog и Cat, которые наследуют от Animal
# и переопределяют метод speak. Создайте объекты этих классов и вызовите метод speak. Это задание поможет вам понять,
# как работает наследование и полиморфизм в Python, а также как переопределять методы в подклассах.


class Animal:
    @staticmethod
    def speak():
        return 'Метод speak класса Animal.'


class Dog(Animal):
    def speak(self):
        return 'Метод speak класса Dog.'


class Cat(Animal):
    def speak(self):
        return 'Метод speak класса Cat.'


# Создание объектов классов Dog и Cat
dog = Dog()
cat = Cat()

print(dog.speak())  # Вывод: Метод speak класса Dog.
print(cat.speak())  # Вывод: Метод speak класса Cat.
