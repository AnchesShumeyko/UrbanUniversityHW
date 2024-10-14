"""Записать и запомнить"""


def custom_write(file_name, strings):
    string_position = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings, start =1):
        first_byte = file.tell()
        file.write(f'{string}\n') #выдает на 1 байт меньше
        # file.write(f'{string} \n') #выдает правильное решение. но там доп пробел!!!!
        string_position[i, first_byte] = string
    file.close()
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
