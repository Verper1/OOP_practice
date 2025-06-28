# Create a class MaxFinder that identifies the largest number in a list.


class MaxFinder:
    def __init__(self, lst: list):
        self.__lst = lst

    def find_max_num(self):
        if not self.__lst:
            return 'Ошибка: Словарь не может быть пустым!'
        return max(self.__lst)


def test_function():
    mf1 = MaxFinder([1, 2, 3, 5])
    mf2 = MaxFinder([2, 10, 21, 3, 6])
    mf3 = MaxFinder([3.01, 2.44, 1.32, 2.56, 3.223])
    mf4 = MaxFinder([])

    assert mf1.find_max_num() == 5
    assert mf2.find_max_num() == 21
    assert mf3.find_max_num() == 3.223
    assert mf4.find_max_num() == 'Ошибка: Словарь не может быть пустым!'
