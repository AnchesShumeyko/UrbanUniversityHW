n = int(input('введите количество строк: '))
m = int(input('введите количество столбцов: '))
value = int(input('введите значение: '))
matrix = []
def get_matrix(n, m, value):
    for i in range(1, n + 1):
        list1 = []
        matrix.append(list1)
        for j in range(1, m + 1):
            list1.append(value)
get_matrix(n, m, value)
print(matrix)

