# Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм, а с помощью
# метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной kg она реализовала методы set_kg()
# - для задания нового значения килограммов, get_kg() - для вывода текущего значения кг. Из-за этого возникло
# неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений.
# Помогите ей переделать класс с использованием функции property() и свойств-декораторов. Код приведен ниже.


class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kilogramms(self):
        return self.__kg

    @kilogramms.setter
    def kilogramms(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')


weight = KgToPounds(12)
print(weight.to_pounds())
print(weight.kilogramms)
weight.kilogramms = 41
print(weight.kilogramms)
weight.kilogramms = 'десять'
