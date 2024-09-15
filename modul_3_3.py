def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(2)

value_list = [3.14, 'кошка', False]
value_dict = { 'a' : 'a dog', 'b' : 'a cat', 'c' : 'a mouse'}
print_params(*value_list)
print_params(**value_dict)

value_list_2 = ['осёл', 15]
print_params(*value_list_2, 42)