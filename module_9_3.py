first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан',  'Компьютер']

first_result = (len(first[i]) - len(second[i]) for i in range(len(first)) if len(first[i]) != len(second[i]))
second_result = (len(first[i]) <= len(second[i]) for i in range(len(first)))

try:
    print(list(first_result))
    print(list(second_result))
except IndexError:
    print(f'разная длина списков')
except TypeError:
    print('один из элементов не является строкой')