def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

                        # Задача 1
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params()

                        # Задача 2
values_list = (2.5, True, [5, 10])
values_dict = {'a': 'bobby', 'b': 2, 'c': 5.1}

print_params(*values_list)
print_params(**values_dict)

                        # Задача 3
values_list_2 = ('пример', 9)
print_params(*values_list_2, 42)

