def calculate_structure_sum(*data_structure):
    sum_ = 0
    for i in data_structure:
        if isinstance(i, (int, float)):
            sum_ += i
        if isinstance(i, str):
            sum_ += len(i)
        if isinstance(i, dict):
            sum_ += calculate_structure_sum(*i.items())
        if isinstance(i, (list, tuple, set)):
            sum_ += calculate_structure_sum(*i)
        if i is None:
            pass
    return sum_

print (calculate_structure_sum([
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]))
