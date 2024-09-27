class House:
    houses_history = []
    __instance = None
    def __new__(cls, name, number_of_floors):
        House.houses_history.append(name)
        cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __str__(self):
        return (f'Название: {self.name}')




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
