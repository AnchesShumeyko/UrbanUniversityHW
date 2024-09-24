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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return(f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}.')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
