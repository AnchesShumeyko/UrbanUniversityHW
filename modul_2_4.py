numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []

for i in numbers:
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                not_prime.append(i)
                break
        else:
            prime.append(i)
print(f'простые числа: {prime}')
print(f'составные числа: {not_prime}')