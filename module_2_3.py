my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]               # исходный список
start = 0                                                            # начальный индекс
number = int(len(my_list))                                           # конечный индекс

while my_list[start] >= 0 and start < number:
    if my_list[start] != 0:
        print(my_list[start])
        start = start + 1
    else:
        start = start + 1                           # ноль не выводится на печать, но не останавливает цикл
else:
    if my_list[start] < 0:
        print('Конец цикла, найдено отрицательное число -', my_list[start])
    if start == number:
        print('Конец цикла - отрицательных чисел не найдено')

