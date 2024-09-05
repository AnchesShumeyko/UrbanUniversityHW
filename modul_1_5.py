immutable_var = ('машина', 2, 3.5, True)
print(immutable_var)
# immutable_var[0] = 'False' #невозможно изменить кортеж, так как он относится к неизменяемой коллекцией
mutable_list = ['Шер', 23, True]
mutable_list.append('Русь')
mutable_list.extend(['Чара', 'Рикки'])
mutable_list.remove(23)
mutable_list.remove(True)
print(mutable_list)






