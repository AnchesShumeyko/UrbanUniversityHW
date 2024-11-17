"""Интроспекция"""


def introspection_info(obj):
    result = []
    result.append(f'Тип объекта: {type(obj)}')
    result.append(f'Атрибуты объекта: {dir(obj)}')
    if callable(obj):
        result.append('Вызываетмость: Да')
    else:
        result.append('Вызываетмость: Нет')
    return '\n'.join(result)


"""класс для поиска факториала переданного числа"""


class FactorialCalculator:
    def __init__(self):
        self.result = 1

    def find_factorial(self, n):
        for i in range(1, n + 1):
            self.result *= i
        return self.result

unknown = 42 # int
unknown = (1, 2, 3) # tuple
unknown = {1, 2, 3}
unknown = {'chapter 1' : 5, 'chapter 2' : 15, 'chapter 3' : 23} # dict
unknown = FactorialCalculator  # class
unknown = FactorialCalculator.find_factorial # function
unknown = "I'm checking different types of objects" #str
unknown = [] # list
number_info = introspection_info(unknown)
print(number_info)
