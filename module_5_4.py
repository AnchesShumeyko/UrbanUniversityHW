class House:
    houses_history = []

    def __new__(cls, *args):
        House.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):  # метод возвращающий кол-во этажей
        return self.number_of_floors

    def __str__(self):  # метод, возвращающий имя и этажи
        return (f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}.')

    # методы для сравнения количества этажей
    def __eq__(self, other):
        if not isinstance(other, int) and not isinstance(other, House):
            return print('ошибка')
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, int) and not isinstance(other, House):
            return print('ошибка')
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, int) and not isinstance(other, House):
            return print('ошибка')
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, int) and not isinstance(other, House):
            return print('ошибка')
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, int) and not isinstance(other, House):
            return print('ошибка')
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, int) and not isinstance(other, House):
            return print('ошибка')
        return self.number_of_floors != other.number_of_floors

    # методы для сложения
    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        elif not isinstance(self, int):
            print('ошибка')

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
