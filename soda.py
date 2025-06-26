# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за
# добавку к выбираемому лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на печать Газировка и
# {ДОБАВКА} в случае наличия добавки, а иначе отобразится следующая фраза: Обычная газировка.


class Soda:
    def __init__(self, adder=""):
        self.adder = adder

    def show_my_drink(self):
        if self.adder:
            return f"Газировка и {self.adder.lower()}"
        else:
            return "Обычная газировка"


cola = Soda()
print(cola.show_my_drink())

pepsi = Soda('Красный сахар')
print(pepsi.show_my_drink())
