# my_list = [1, 2, 3, 4, 5]
#
# # на этой стадии нет значений
# gen = (x * x for x in my_list) # для каждого значения x из my_list вернем list
#
# print(gen) # <generator object <genexpr> at 0x105257510>
# print(type(gen))
#
# for i in gen:
#     print(i)



# changing_gen = (x ** x for x in my_list) # в кубе
# # генератор по условию
# condition_gen = (x for x in my_list if x % 2 == 0)
#
# print(list(changing_gen))
# print(list(condition_gen))
#
# print(my_list)


# r = range(0, 10, 2) # генератор последовательности, 2 — шаг
#
# print(r)
# print(type(r))
# print(list(r))
#
# for i in range(10):
#     print(i)


# генератор списков
my_list = [1, 2, 3, 4, 5]
list_gen = [x for x in my_list] # когда квадратные скобки, то создаем не генератор, а новый список
# c помощью генератора списков

print(list_gen)
print(type(list_gen))

changing_list_gen = [x ** x for x in my_list]
conditional_list_gen = [x for x in my_list if x % 2 == 0]

print(changing_list_gen)
print(conditional_list_gen)


# генератор словарей
# my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
#
# dict_gen = {k: v for k, v in my_dict.items() if k % 2 == 0}
# list_gen = [k * k for k in my_dict.keys()]
# print(dict_gen) # {2: 2, 4: 4}
# print(list_gen)


keys = [1, 2, 3, 4, 5]
values = [11, 12, 13, 14, 15]

print(list(zip(keys, values))) # [(1, 11), (2, 12), (3, 13), (4, 14), (5, 15)]

di = {k: v for k, v in zip(keys, values)} # zip объединить две последовательности друг с другом
print(di)

