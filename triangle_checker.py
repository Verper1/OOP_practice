# Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        print(self.is_triangle())

    def is_triangle(self):
        if (type(self.a) not in [int, float]) or (type(self.b) not in [int, float]) or (type(self.c) not in [int, float]):
            return "Нужно вводить только числа!"
        elif self.a < 0 or self.b < 0 or self.c < 0:
            return "С отрицательными числами ничего не выйдет!"
        elif self.a + self.b <= self.c or self.c + self.b <= self.a or self.c + self.a <= self.b:
            return "Жаль, но из этого треугольник не сделать."
        else:
            return "Ура, можно построить треугольник!"


triangle1 = TriangleChecker(2, 3, 4)
triangle2 = TriangleChecker(77, 3, 4)
triangle3 = TriangleChecker(77, 3, 'Сторона3')
triangle4 = TriangleChecker(77, -3, 4)
