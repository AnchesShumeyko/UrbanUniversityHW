class House(): #создаем класс "House"
    def __init__(self, name, number_of_floors):
        self.name = name # определяем атрибут имя(название здания)
        self.number_of_floors = number_of_floors # определяем атрибут количества этажей

    def go_to(self, new_floor): # метод для "лифта" :-)
        for floor in range(new_floor):
            if new_floor <= self.number_of_floors: # задаем условие, что едем до этажа, только если
                                                        # он ниже чем кол-во этажей в здании
                print(floor + 1)
            else:
                print('Такого этажа не существует')
                break

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

# нужно же поиграться:
h3 = House('7-ое Небо', 115)
h3.go_to(57)
h3.go_to(120)