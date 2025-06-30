# Last Digit in Words: Write a class with a method that takes an integer and
# prints the last digit of that number in words.


class Num:
    nums = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре', 5: 'Пять', 6: 'Шесть', 7: 'Семь', 8: 'Восемь', 9: 'Девять',
            0: 'Ноль'}

    def __init__(self, num: int):
        self.num = num

        print(self.last_digit())

    def last_digit(self):
        self.num = str(self.num)[-1:]
        return self.num


n1 = Num(212354321)
