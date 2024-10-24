def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
            try:
                result += i
            except TypeError:
                print(f'некорректный тип данных для подсчета суммы - {i}')
                incorrect_data += 1
    except TypeError:
        return result, incorrect_data
    return result, incorrect_data


def calculate_average(numbers):
    total_sum, incorrect_data = personal_sum(numbers)
    try:
        result = total_sum / (len(numbers) - incorrect_data)

    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None

    except ZeroDivisionError:
        return 0
    return result


# Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
