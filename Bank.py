# Создайте класс BankAccount с приватным атрибутом balance. Реализуйте методы для депозита, снятия и проверки баланса.
# Используйте методы доступа для работы с приватным атрибутом. Это задание поможет вам понять, как использовать
# инкапсуляцию для защиты данных и как реализовать методы доступа для работы с приватными атрибутами.


class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def withdraw(self, money):
        if 0 < money < self.__balance:
            self.__balance -= money
            return self.__balance
        else:
            return 'Ошибка: Нельзя снять деньги, если у вас 0 или меньше денег, чем вы хотите снять!'

    def deposit(self, money):
        self.__balance += money
        return self.__balance


# Тесты в Bank_test.py
