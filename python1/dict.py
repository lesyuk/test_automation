# Словарь - набор ключей и значений

# Создание пустого словаря
empty_dict = {}

# Второй способ
empty_dict = dict()

# Словарь, так же как и списки - изменяемый тип: можем добавлять, изменять, удалять ключи/значения
# Добавление ключа в словарь происходит через []
empty_dict['key1'] = 'value1'
print(empty_dict) # {'key1': 'value1'}
empty_dict['key2'] = 'value2' # Добавление еще одного ключа в конец
print(empty_dict) # {'key1': 'value1', 'key2': 'value2'}

# Eсли мы попробуем изменить наше значение существующего ключа, то он спокойно изменится
empty_dict['key2'] = 'value2222222'
print(empty_dict) # {'key1': 'value1', 'key2': 'value2222222'}

# Cловарь можно дополнить  другим словарем. Добавляем через {} если хотим не добавлять, а создавать элемент
empty_dict.update({'key3': 'value3'})
print(empty_dict) # {'key1': 'value1', 'key2': 'value2222222', 'key3': 'value3'}
print(empty_dict['key3']) # печатаем значение ключа value3

"""
В большинстве случаев ключами будут являться строки, но это не все. Ключ 
который создается в словаре должен быть строго НЕизменяемым, для того чтобы словарь не имел пересечений по ключам 
т.е. мы неможем создать словарь, у которого ключом будет список: {[]: 123} // TypeError: unhashable type: 'list' 
ошибка означает что он попытался захэшировать ключ, т.е. получить уникальный хэш, а как мы знаем, если объект 
изменяемый, его кэш будет постоянно меняться, а в словаре это запрещено и поэтому ключами могут быть только 
неизменяемые типы это может быть int, float (не рекомендуется), tuple, string
"""

print({1: 123}) # {1: 123}
# print({{}: 123}) # другой словарь тоже не может быть ключам // unhashable type: 'dict'

# Значением может быть что угодно
# Так же как в списках нет никаких ограничений, может сделать хоть словарь в словаре и еще в одном словаре
print({1: {2: {3: {}}}}) # {1: {2: {3: {}}}} // вложенность можно сделать бесконечную и объекты могут быть внутри всех типов
# Это очень похоже на JSON, еще поговорим про это

# Можно итерироваться по словарям
di = {1: 2, 3: 4, 5: 6}
di.items() # Список из тюплов где первый элемент это ключ, второй значение
print(di.items()) # dict_items([(1, 2), (3, 4), (5, 6)])
print(di.values()) # Вернется список со всеми значениями // dict_values([2, 4, 6])
print(di.keys()) # Вернется список со всеми ключами // dict_keys([1, 3, 5])

# Сортировка. у словаря нет метода sort() потому что в целом эти хэшмапы беспорядочны
# (с 3.6 запоминается порядок, но не сортируется)
print(sorted(di)) # [1, 3, 5] Отсортированный список ключей
# print(sorted(di,reversed=True)) # 'reversed' is an invalid keyword argument for sort()

# Сортировка по значениям
# метод sorted принимает еще ключ по тому как ему сортировать
di = {1: 1, 3: 7, 5: 2}
# В sorted попадут ключи, на каждый ключ вызовется di.get который отдаст значение
print(sorted(di, key=di.get)) # di.get позволяет отсортировать ключи по сортировке их значений, а не самих ключей
# [1, 5, 3] // в этом случае критерием сортировки будет значение (1 = 1, 5 = 2, 3 = 7)
# Когда мы вызываем list на словарь, мы получаем ключи
print(list(di)) # [1, 3, 5]
print(list(di.values())) # [1, 7, 2]

# Boolean
print(bool({})) # False
print(bool({1: 1})) # True
