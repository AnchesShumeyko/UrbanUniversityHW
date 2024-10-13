from math import pi

""" Обший класс для фигуры в целом"""


class Figure:
    sides_count = 0  # количество сторон в фигуре

    def __init__(self, color: tuple, *sides, filled=False):  # список RGB, стороны, заливка фигуры
        self.__color = color
        self.__sides = sides
        if len(self._Figure__sides) != self.sides_count:  # условия для неправильного ввода кол-ва сторон
            self._Figure__sides = [1 for i in range(self.sides_count)]
        else:
            self._Figure__sides = [i for i in sides]
        self.filled = filled

    def __repr__(self):
        return f'{self.__color}, {self.__sides}, {self.filled}, {self.sides_count}'

    def get_color(self):  # геттер для цвета
        return self.__color

    def __is_valid_color(self, r, g, b):  # валидация RGB на допустимые значения
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):  # сеттер для получения цветом
        if self.__is_valid_color(r, g, b) == True:
            self.__color = (r, g, b)

    def get_sides(self):  # геттер для сторон
        return self.__sides

    def is_valid_sides(self, new_sides):  # валидация вводимых сторон
        if len(new_sides) != len(self.__sides):  # если кол-во не равно предыдущему
            return False
        if not all(isinstance(num, int) for num in new_sides):  # если числа в списке не являются целыми
            return False
        else:
            return True

    def set_sides(self, *new_sides):  # сеттер для введения новых значений сторон
        if self.is_valid_sides(new_sides) == True:
            self.__sides = list(new_sides)  # если валидны - отдает список новых сторон
        else:
            return self.__sides  # если нет - возвращает предыдущее значение

    def __len__(self):
        return sum(self.__sides)


""" класс для круга, переопределен инит с введением радиуса и заливкой фигуры"""


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, *sides, radius=0):
        super().__init__(color, *sides, filled=True)
        self.__radius = self.__len__() / (2 * pi)

    def get_square_side(self):  # площадь круга из периметра
        for i in self._Figure__sides:
            sq = i ** 2 / (4 * pi)
            return sq

    def get_square_rad(self):  # площадь круга из радиуса
        s = pi * self.__radius ** 2
        return s


"""класс для треугольника"""


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, *sides):  # инит переопределен для заливки фигуры, можно было и не делать
        super().__init__(color, *sides, filled=True)

    def get_square(self):  # получение площади треугольника
        p = 0.5 * (sum(self._Figure__sides))
        s2 = p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2])
        s = s2 ** 0.5
        return s


""" класс для куба"""


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides):  # переопределение инита и условий отбора количеста введеных сторон
        super().__init__(color, sides, filled=False)
        if len(sides) == 1:  # переопределение метода "отбраковки" вводимых значений
            for i in sides:  # цикл для "отрисовки" сторон
                self._Figure__sides = [i for j in range(self.sides_count)]  # по вводимому числу
        else:
            self._Figure__sides = [1 for i in range(self.sides_count)]  # меняем на 1 неверный ввод

    def get_volume(self):  # получение объема куба
        for i in self._Figure__sides:
            volume = i ** 3  # одна сторона возводимая в куб
            return volume

    def set_sides(self, *new_sides):  # переопреление сеттера для куба
        if self.is_valid_sides(new_sides) == True:
            for i in new_sides:
                self._Figure__sides = list(i for j in range(self.sides_count))
        else:
            return self._Figure__sides

    def is_valid_sides(self, new_sides):  # переписала метод валидации, только из-за первой строчки
        if len(new_sides) != 1:
            return False
        if not all(isinstance(num, int) for num in new_sides):
            return False
        else:
            return True


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())

## Tests for Fugure
# f1 = Figure((100,100,100), 10, 3, 6)
# print(f1)
# print(f1.get_sides())
# print()
# f2 = Figure((200,200,200), 2,3)
# print(f2)
# print(f2.get_sides())
# print()
# f3 = Figure((3,3,3), 15, 1, 3)
# print(f3)
# print(f3.get_sides())
# f3.set_sides(2,4)
# print(f3.get_sides())
# f3.set_sides(2.5,4,6)
# print(f3.get_sides())
# f3.set_color(300, 200, 100)
# print(f3.get_color())

# TEST FOR CIRCLES
# crl1 = Circle((1, 1, 1), 20)
# print(crl1)
# crl2 = Circle((2, 2, 2), 20, 30, 40)
# print(crl2)
# crl2.set_color(259, 260,0)
# print(crl2.get_color())
# crl2.set_sides(15)
# print(crl2.get_sides())
# crl2.set_sides(10.3)
# print(crl2.get_sides())
# print(crl1)
# print(crl1.get_square_side())
# print(crl1.get_square_rad())
#
# # TEST FOR TRIANGLE
# tr1 = Triangle((1, 1, 1), 10, 10)
# tr2 = Triangle((2, 2, 2), 5, 6, 7)
# print(tr1)
# print(tr2)
# tr1.set_color(10,10,10)
# print(tr1.get_color())
# tr1.set_color(100,200,300)
# print(tr1.get_color())
# tr1.set_sides(10)
# tr1.set_sides(20,3.5, 4)
# tr1.set_sides(9, 10, 11)
# print(tr1.get_sides())
# print(tr1.get_square())
# #
# TEST FOR CUBE
# c1 = Cube((1,1,1),9)
# print(c1)
# print(c1.get_volume())
# c1.set_sides(2,2)
# c2 = Cube((2,2,2), 2,2)
# print(c2)
# c2.set_sides(3)
# print(c2.get_sides())
# print(c2.get_volume())
# print(Circle.mro())