from decimal import Decimal

""" 
            "Программистам всё можно"
            
функция сложения переданных значений, которыми могут быть: float, int и str
"""


def add_everything_up(a, b):
    # если передано значение float, перевожу float в decimal (а вдруг это финансовые сложения или медицинские данные)
    if isinstance(a, float):
        a = Decimal(str(a))
    if isinstance(b, float):
        b = Decimal(str(b))
    # исключения-уловитель, если вдруг передали str
    try:
        c = a + b
        return c

    except TypeError:
        c = f'{a}{b}'
        return c


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
