# Пустой сет можно задать только одним образом
empty_set = set()
# Непустой можно так же таким образом
my_set = {1, 2, 3, 4, 5}

# Множество хранит в себе строго уникальные элементы
# Очень удобно когда мы хотим уникализировать какую-то последовательность и получить только уникальные элементы
lst = [1,1,2,3,3,4,5]
# Получаем множество уникальных элементы из списка
print(set(lst)) # {1, 2, 3, 4, 5}

# Множество - изменяемый тип
my_set.add(7)
my_set.add(7) # Сколько бы раз не добавляли 7 он не добавится, т.к. у же есть
my_set.add(7)
my_set.add(7)
my_set.add(7)
print(my_set) # {1, 2, 3, 4, 5, 7}

my_set.remove(7)
print(my_set) # {1, 2, 3, 4, 5}

# Методы пересечений множеств: объединение, пересечение, разность, изометрическая разность, неизменяемые множества
# TBD
print(type(my_set)) # <class 'set'>
