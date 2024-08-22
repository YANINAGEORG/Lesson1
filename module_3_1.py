calls = 0
def count_calls(calls):  # функция счетчик
    calls += 1

def string_info(string):
    return len(string), string.upper(), string.lower()
    count_calls()

def is_constains(string, list_to_search):
    if string.lower() in list(map(str.lower, list_to_search)):
        print(string, list_to_search, True)
    else:
        print(string, list_to_search, False)
    count_calls()


print(string_info('Refrigerator'))
print(string_info('ElefANT'))

print(is_constains('Yana', ['Bob', 'APPYANA', 'yaNa']))
print(is_constains('YaniNA', ['Boby', 'APPYANINA', 'yaNa']))

print(calls)




