class House():  # создаем класс "House"
    def __init__(self, name, number_of_floors):
        self.name = name  # определяем атрибут имя(название здания)
        self.number_of_floors = number_of_floors  # определяем атрибут количества этажей

    def go_to(self, new_floor):  # метод для "лифта" :-)
        for floor in range(new_floor):
            if new_floor <= self.number_of_floors:  # задаем условие, что едем до этажа, только если
                # он ниже чем кол-во этажей в здании
                print(floor + 1)
            else:
                print('Такого этажа не существует')
                break

    def __len__(self): #метод возвращающий кол-во этажей
        return self.number_of_floors

    def __str__(self): # метод, возвращающий имя и этажи
        return (f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}.')

#методы для сравнения количества этажей
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
        if not isinstance(other, int):
            return print('ошибка')
        return self

    def __radd__(self, other):
        self.number_of_floors = other + self.number_of_floors
        return self

    def __iadd__(self, other):
        self.number_of_floors += other
        return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + '10' # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
