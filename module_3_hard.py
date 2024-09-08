def calculate_structure_sum(data_structure):
    data_structure = []
    sum_ = 0

    for i in data_structure:

        while data_structure[i] is not int():

            if type(i) is str():
                i = len(i)
                return i

            if type(i) is list() or type(i) is tuple():
                data_structure.append(*i)
                return i

            if type(i) is dict():
                data_structure.append(**i)
                return i

        data_structure = sum(data_structure)

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

