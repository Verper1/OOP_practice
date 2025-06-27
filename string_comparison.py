# Строки в Питоне сравниваются на основании значений символов. Т.е. если мы захотим выяснить, что больше: Apple или
# Яблоко, – то Яблоко окажется бОльшим. А все потому, что английская буква A имеет значение 65 (берется из таблицы
# кодировки), а русская буква Я – 1071 (с помощью функции ord() это можно выяснить).
# Такое положение дел не устроило Анну. Она считает, что строки нужно сравнивать по количеству входящих в них символов.
#
# Для этого девушка создала класс RealString и реализовала озвученный инструментарий. Сравнивать между собой можно
# как объекты класса, так и обычные строки с экземплярами класса RealString.
# К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного.

# class RealString:  # Собственные потуги.
#     def __init__(self, string1: str, string2: str):
#         self.string1 = string1
#         self.string2 = string2
#
#         print(self.check_str(string1, string2))
#
#     def check_str(self, string1, string2):
#         number_of_letters1 = sum(1 for letter in string1)
#         number_of_letters2 = sum(1 for letter in string2)
#         if number_of_letters1 > number_of_letters2:
#             return f'Больше слово: {number_of_letters1}'
#         else:
#             return f'Больше слово: {number_of_letters1}'

from functools import total_ordering  # Чтобы повторить класс, придуманный Анной (с тремя методами),
                                      # требуется воспользоваться декоратором @total_ordering из модуля functools
                                      # (упрощает реализацию сравнений. Требует лишь 2 дополняющих варианта сравнения -
                                      # например, больше и равно - чтобы автоматически "дописать" остальные).

@total_ordering
class RealString:
    def __init__(self, some_str):
        self.some_str = str(some_str)

    def __eq__(self, other):  # __eq__() – для равенства ==
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.some_str) == len(other.some_str)

    def __lt__(self, other):  # __lt__() – для оператора меньше <
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.some_str) < len(other.some_str)


# Тесты
str1 = RealString('Молоко')
str2 = RealString('Абрикосы растут')
str3 = 'Золото'
str4 = [1, 2, 3]
print(str1 < str4)
print(str1 >= str2)
print(str1 == str3)

# __eq__() – для равенства ==
# __ne__() – для неравенства !=
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=
