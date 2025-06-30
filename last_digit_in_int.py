# Last Digit in Words: Write a class with a method that takes an integer and
# prints the last digit of that number in words.


class Num:
    nums = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре', 5: 'Пять', 6: 'Шесть', 7: 'Семь', 8: 'Восемь', 9: 'Девять',
            0: 'Ноль'}

    def last_digit(self, num):
        last_num = int(str(num)[-1:])
        answer = self.nums.get(last_num)
        return answer


def test_func():
    n1 = Num()
    for i in range(10, 20):
        assert n1.last_digit(i) == n1.nums.get(int(str(i)[-1:]))
