first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))
third = float(input('Введите третье число: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else: print(0)
