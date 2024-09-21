def count_data(data_structure):
    n = 0
    for i in data_structure:
        if isinstance(i, int):
            n += i
        elif isinstance(i, str):
            n += len(i)
        elif isinstance(i, dict):
            n += count_data(list(i.items()))
        elif isinstance(i, list):
            n += count_data(i)
        elif isinstance(i, tuple):
            n += count_data(i)
        elif isinstance(i, set):
            n += count_data(i)

    return n

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = count_data(data_structure)
print(result)
