def get_matrix(n, m = 0, value = 0):
    matrix = []
    for i in range(1, n + 1):
        list1 = []
        matrix.append(list1)
        for j in range(1, m + 1):
            list1.append(value)
    print(matrix)

get_matrix(2,2,10)
get_matrix(3,5,42)
get_matrix(4,2,13)
get_matrix(0)
