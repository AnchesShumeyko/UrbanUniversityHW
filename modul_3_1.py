calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    a = string.lower()
    b = string.upper()
    c = len(string)
    return c, a, b

def is_contains(string, list_ = []):
    count_calls()
    a = string.lower()
    for i in list_:
        b = i.lower()
        if a == b:
            return True
    if a != b:
        return False

    return a, b


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
