class Car:
    def __init__(self, model: str, vin: int, numbers):
        self.model = model
        self._vin = vin
        self._numbers = numbers

        self._is_valid_vin(vin)
        self._is_valid_number(numbers)

    def _is_valid_vin(self, vin_number): # поменять местами
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(f'Некорректный ти vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера')
        else:
            return True

    def _is_valid_number(self, numbers):
        if not isinstance (numbers, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers(f'Неверная длина номера')
        else:
            return True
    def __str__(self):
        return f'{self.model} - {self._vin} - {self._numbers}'

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')