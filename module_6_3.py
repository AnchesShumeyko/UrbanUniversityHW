""" примечание к работа:
можно было не делать прямого обращения к инитам родителей в классе Pegasus, а сделать переопределение инита в 
классе Horse (оно закомментировано после апробации). Тогда в классе Pegasus, можно было бы инит пропустить"""


class Horse:

    def __init__(self, x_distance=0, sound='Frrr'): # переопределение инита, так как добавляем от Орла
        self.x_distance = x_distance
        self.sound = sound
        # super().__init__(y_distance=0, sound='I train, eat, sleep,and repeat')

    def run(self, dx):
        self.x_distance += dx
        return self


class Eagle:

    def __init__(self, y_distance=0, sound='I train, eat, sleep,and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy
        return self


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance=0,  y_distance=0): # этот метод можно убрать, если добавить в инит Horse super от Eagle
        Horse.__init__(self)
        Eagle.__init__(self)


    def move(self, dx, dy):
        self.run(dx), self.fly(dy)
        return self

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
# print(issubclass(Pegasus, Horse))
# print(issubclass(Pegasus, Eagle))
# print(issubclass(Horse, Eagle))
# print(issubclass(Eagle, Horse))
print(Pegasus.mro())

