numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
end_ = numbers[-1] + 1
check = list(range(2,end_))

primes = []                        # список простых чисел
not_primes = []                    # список не простых чисел

for i in numbers:
    if i == 1:                      # исключаем единицу из выборки
        continue
    for j in check:
        if i in not_primes:         # исключаем повторное включение одного и того же элемента в список
            continue
        if j < i and i % j == 0:
            not_primes.append(i)    # заполняем список не простых чисел

for i in numbers:
    for k in not_primes:
        if i in primes or i == 1 or i in not_primes:        # исключаем из выборки единицу и повторения
            continue
        if numbers != not_primes:
            primes.append(i)                                # заполняем список простых чисел

print('Список простых чисел:', primes)
print('Список не простых чисел:', not_primes)









