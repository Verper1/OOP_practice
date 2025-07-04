# Polymorphism with a Function: Create a function describe_pet that takes an object of Animal and calls
# its speak method, demonstrating polymorphism.


class Animal:
    def speak(self):
        print('Метод speak Animal')


class Cat(Animal):
    def speak(self):
        print('Метод speak Cat')


def speak(animal):
    animal.speak()


a1 = Animal()
c1 = Cat()

speak(a1)
speak(c1)
