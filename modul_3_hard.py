def calculate_structure_sum(data_structure):
    n = 0
    for i in data_structure:
        if isinstance(i, int):
            n += i
        elif isinstance(i, str):
            n += len(i)
        elif isinstance(i, dict):
            n += calculate_structure_sum(list(i.items()))
        elif isinstance(i, list):
            n += calculate_structure_sum(i)
        elif isinstance(i, tuple):
            n += calculate_structure_sum(i)
        elif isinstance(i, set):
            n += calculate_structure_sum(i)

    return n

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
