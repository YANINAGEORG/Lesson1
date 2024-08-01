# домашнее задане - кортежи

immutable_var = True, 6, 'big_boss', [7, 8]
print(immutable_var)

# immutable_var[1] = 60

# получаем ошибку - TypeError: 'tuple' object does not support item assignment, т.к. пытаемся изменить неизменяемый элемент кортежа типа число

mutable_list = ['white', 'blue', 'black', 'grey']
mutable_list[2] = 'red'
print(mutable_list)

