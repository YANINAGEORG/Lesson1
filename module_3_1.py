calls = 0
def count_calls():  # функция счетчик
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()



def is_constains(string, list_to_search):
    count_calls()
    if string.lower() in list(map(str.lower, list_to_search)):
        print(string, list_to_search, True)
    else:
        print(string, list_to_search, False)


print(string_info('Refrigerator'))
print(string_info('ElefANT'))

is_constains('Yana', ['Bob', 'APPYANA', 'yaNa'])
is_constains('YaniNA', ['Boby', 'APPYANINA', 'yaNa'])

print(calls)




