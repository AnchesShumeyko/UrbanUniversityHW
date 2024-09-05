my_dict = {'Рикки': 2018, 'Шер': 2021, 'Чара': 2023, 'Русь': 2023}
print(my_dict)
print(my_dict['Шер'])
print(my_dict.get('Мася'))
my_dict.update({'Кошмарик': 2016,
               'Тима': 2014})
print(my_dict)
angry = my_dict.pop('Тима')
print(angry)
print(my_dict)
#множества
my_set = {1, 13, 25, 'собака', 'кошка', 3.14, 13, 76, 'кошка'}
print(set(my_set))
my_set.add(('птица', 'кит'))
my_set.discard(3.14)
print(my_set)


