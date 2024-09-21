def calculate_structure_sum(data_structure):
    n = 0
    for v in data_structure:
        if isinstance(v, int):
            n += v
        elif isinstance(v, str):
            n += len(v)
        elif isinstance(v, dict):
            n += calculate_structure_sum(list(v.items()))
        elif isinstance(v, list):
            n += calculate_structure_sum(v)
        elif isinstance(v, tuple):
            n += calculate_structure_sum(v)
        elif isinstance(v, set):
            n += calculate_structure_sum(v)

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