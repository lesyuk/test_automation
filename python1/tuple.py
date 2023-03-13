empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple) # () # пустой кортеж
# обычно tuple создается из какой-то последовательности, пустой создавать нет смысла
tpl = tuple([1, 2, 3, 4, 5])
tpl1 = tuple('1234567')

print(tpl) # (1, 2, 3, 4, 5)
print(tpl1) # ('1', '2', '3', '4', '5', '6', '7')

# можно обращаться по индексам
print(tpl[0]) # 1
print(tpl[-1]) # 5

# если мы попробуем кортеж изменить, то не получится
# tpl[1] = 2 Tuples don't support item assignment

tpl2 = (0, 0, 0)
tpl3 = (0)
print(tpl2) # (0, 0, 0) // кортеж
print(tpl3) # 0 // число
tpl4 = (1) # 0 // число
print(tpl4) # 1 // число
tpl5 = ('a')
print(tpl5) # 'a' // строка

print(bool(()))
print(bool((0))) # по примеру вышы видно что если в кортеже один элемент то это не кортеж а просто число / строка и тд
# а так как 0 это False то и получаем