class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Can't divide by zero!"

# Создать экземпляр класса `Calculator`:
calculator = Calculator()
# Выполнить сложение и вывести результат:
result = calculator.add(7, 5)
print("7 + 5 =", result)
# Выполнить вычитание и вывести результат:
result = calculator.subtract(34, 21)
print("34 - 21 =", result)
# Выполнить умножение и вывести результат:
result = calculator.multiply(54, 2)
print("54 * 2 =", result)
# Выполнить деление и вывести результат:
result = calculator.divide(144, 2)
print("144 / 2 =", result)
# Попытаться выполнить деление на ноль, что вызывает ошибку, и вывести сообщение об ошибке:
result = calculator.divide(45, 0)
print("45 / 0 =", result)
