def is_prime(func):
    def wrapper(*args):
        our_sum = func(*args)
        for i in range(2, our_sum):
            if (our_sum % i) == 0:
                print(f'составное')
                break
            else:
                print(f'простое')
                break
        return our_sum
    return wrapper

@is_prime
def sum_three(*args):
    total = 0
    for i in args:
        total += i
    return total


result = sum_three(2, 3, 6)
print(result)