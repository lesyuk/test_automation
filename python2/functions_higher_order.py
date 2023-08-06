# # Функции высшего порядка - это функции, которые принимают на вход другую функцию (не результат, а саму функцию)
#
# list1 = [7, 2, 3, 10, 12]
# list2 = [-1, 1, -5, 4, 6]
#
#
# def multiply(x, y):
#     return x * y
#
# # map - одна из встроенных в python функций высшего порядка. всего таких 3
# # map принимает функцию и последовательность (любое количество итерируемых объектов).
# # Главное, чтобы количество последовательностей совпадало с количество аргументов у функции
# # если количество элементов в итерируемых объектах будет несовпадать map посчитает по меньшему количеству
# res1 = map(multiply, list1, list2) # multiply - объект функции
# # 1. Берем по 1 элементу из каждой последовательности
# # 2. Вызываем функцию multiply
# # 3. Передаем значения элементов в функцию
# # 4. Получаем каждое возвращенное значение и выстраиваем друг за другом
# print(list(res1)) # [-7, 2, -15, 40, 72]
#
# # res2 = map(lambda x, y: x * y, list1, list2) # тоже самое
# # print(list(res2)) # [-7, 2, -15, 40, 72]
#
# # можно использовать любой итерируемый объект
res2 = map(lambda x, y: x * y, 'adb', [1, 2, 3])
print('Map result', list(res2)) # ['a', 'dd', 'bbb']
#
#

# filter - отфильтровать что-то по какому-то условию
# numbers = [10, 4, 2, -1, 6]
#
# # хочу оставить в списке элементы меньше 5
# def lower_then_5(x):
#     return x < 5 # возвращает True или False
#
# # функция высшего порядка filter принимает на вход функцию и значение
# res = filter(lower_then_5, numbers)
# print(list(res))
#
# # тоже самое
# res2 = filter(lambda x: x < 5, numbers)
# print(list(res2))
#
# # еще пример
# res3 = filter(lambda s: s == 'a', 'asddfokfwqpldpsaldpsaalpqdc,as,da,')
# print(list(res3)) # ['a', 'a', 'a', 'a', 'a', 'a']


# с версии 3 reduce не в билдинах, функция высшего порядка
from functools import reduce

numbers = [2, 3, 4, 5, 6] # sum 20

def add(temp_result, x):
    return temp_result + x

res1 = reduce(add, numbers)
# reduce на 1 итерации берет 2 первых значения списка
# на 1 итерации возьмет 2 (temp_result) и 3 (x), сохранит 5
# на 2 итерации 5 (результат вычисления предыдущей функции) и 4, сохранит 9 и тд
# 2 + 3
# 5 + 4
# 9 + 5
# 14 + 6 == 20
print(res1) # 20

# тоже самое
res2 = reduce(lambda temp_result, x: temp_result + x, numbers)
print('Reduce reslut:', res2)

# встроенный sum в питоне
res3 = sum(numbers)
print(res3)


def minus(temp_result, x):
    return temp_result - x


res4 = reduce(minus, numbers)
print(res4) # -16