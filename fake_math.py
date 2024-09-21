#создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать строку 'Ошибка'.

def divide(first, second):
    if second != 0:
        return first / second
    elif second == 0:
        return 'ошибка'
