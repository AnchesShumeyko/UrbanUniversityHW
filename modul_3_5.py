def get_multiplied_digits(n):
    str_n = str(n) # переводим в строки
    str_number = str_n.replace('0', '') # отбрасываем нули

    first = int(str_number[0])
    
    if len(str_number) == 1:
        return first
    if len(str_number) > 1:
        if first != '0':
            return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(40203))
print(get_multiplied_digits(420)) 
