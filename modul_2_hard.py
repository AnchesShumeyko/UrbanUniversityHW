def password_get():
    for num in range(3, 21): # раскладываем цифры камня по вертикали
        password = []       # создаем список пароля для каждого значения камня

        # цикл для подбора пар сумме кратности для камня
        for i in range(1, 20):
            for k in range(1, 20):
                sum = (k+i)

                if num % sum == 0 and k != i:
                    password.append([i, k])

                if num % sum!= 0:
                    continue
# выбор для уникальных пар из образованных в пароле
        for pairs in password: #раскладка по парам
            pairs.sort() #сортировка значений в паре
        password.sort() # сортировка пар (получаем одинаковые пары в пароле друг за другом)

        for p in password: # удаляем повторные пары
            while password.count(p) > 1:
                password.remove(p)

        #объединяем пары в пароле в один список
        flat_pass = []
        for group in password:
            for i in group:
                flat_pass.append(i)


        print(f'{num} : {flat_pass}')
password_get()

# понимаю, что было бы хорощо все это написать разными функциями,
# но не могу разобраться пока с флагами

# как удалить запятые и скобки списка тоже пока не понимаю


