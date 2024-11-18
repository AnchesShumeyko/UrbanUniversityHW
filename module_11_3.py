from pprint import pprint

""" Интроспекция"""


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr)) and not attr.startswith('__')]
    module = obj.__class__.__module__
    result = {
        'тип объкта': obj_type,
        'атрибуты': attributes,
        'методы': methods,
        'модуль': module
    }

    return result


# Пример использования функции с собственным классом
class FactorialCalculator:
    def __init__(self):
        self.result = 1

    def find_factorial(self, n):
        for i in range(1, n + 1):
            self.result *= i
        return self.result


# Тестирование функции
number_info = introspection_info(42)
pprint(number_info)

my_class_info = introspection_info(FactorialCalculator())
pprint(my_class_info)
