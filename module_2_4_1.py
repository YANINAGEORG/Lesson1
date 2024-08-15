numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []                        # список простых чисел
not_primes = []                    # список не простых чисел

is_prime = True                     # флаг, True - в prime, False - в not_prime

for i in range(1, len(numbers)):
    cur = numbers[i]
    for j in range(2, cur // 2 + 1):
        if cur % j == 0:
            is_prime = False
            if cur not in not_primes:
                not_primes.append(cur)
        else:
            is_prime = True

    if is_prime:
        primes.append(cur)

print('Список простых чисел:', primes)
print('Список не простых чисел:', not_primes)





