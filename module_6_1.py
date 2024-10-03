"""
переделанное ДЗ. В предыдущей версии метод eat был в классе Animal. По задаче должен был
находиться в Mammal и Predator. По мне логичнее его было оставить в родительском классе, так как
это свойство хорактерно для всех животных, даже кораллов. Но переделала, хотя это дублирование кода.

если не будет сложно, объясните,пожалуйста, почему именно так просили переделать?

"""


class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True

        if food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predator(Animal):

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True

        if food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant():
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(p2.name)

print(a1.alive)
print(a2.fed)

#
a1.eat(p1)

a2.eat(p2)
print(a1.alive)
print(a2.fed)
