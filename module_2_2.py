first = input('Введите первое число - ')
second = input('Введите второе число - ')
third = input('Введите третье число - ')

if first != second and second != third and first != third:
    print('Количество одинаковых чисел - 0')
if (first == second and first != third) or (second == third and first != second) or (first == third and first != second):
    print('Количество одинаковых чисел - 2')
if first == second and second == third:
    print('Количество одинаковых чисел - 3')
