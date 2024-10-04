def test_function():
    def inner_function():
        print("Я в области видимости функции, test_function")
    inner_function()

test_function()
# inner_function()     # проверка, что вложенную функцию нельзя вызвать извне
# test_function.inner_function()
# inner_function(test_function())

