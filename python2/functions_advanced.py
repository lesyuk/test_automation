# def add(x, y):
#     return x + y
#
#
# r1 = add(1, 10)
# print(r1) # 11
#
# r2 = add('abc', 'def')
# print(r2) # 'abcdef'

# def func():
#     pass
#
# print(func()) # None

# def func (a, b, c=2): # a, b - позиционные аргументы, c=2 - именованные аргументы (всегда идут после позиц.)
#     return a + b + c
#
# r1 = func (1, 2) # a = 1, b = 2, c = 2
# print(r1) # 5
#
# r2 = func (1, 2, 3) # a = 1, b = 2, c = 3
# print(r2) # 6
#
# r3 = func (1, b=2, c=3)
# print(r3) # 6

# r4 = func (a=3, c=6) # TypeError: func() missing 1 required positional argument: 'b'
# print(r4) # 9

# r5 = func (1, 2, b=6)
# print(r3) # TypeError: func() got multiple values for argument 'b'

# def func (*args): # любое количество позиционных аргументов, в т.ч. 0
#     return args

# r1 = func(1, 2, 3, 'abc', 'adsasasa', '1111    ')
# print(r1) # (1, 2, 3, 'abc', 'adsasasa', '1111    ')

# r1 = func(1, 2, 3, 'abc', 'adsasasa', '1111    ', b=1)
# print(r1) # : func() got an unexpected keyword argument 'b'
#
# r2 = func()
# print(r2) # ()
#
# r3 = func(1)
# print(r3) # (1,) - скобки подсказывают, что это tuple из 1-го элемента

# def func(**kwargs): # любое количество позиционных аргументов, в т.ч. 0, **kwargs - словарь(ключ - значение)
#     return kwargs
#
#
# r1 = func(a=1, b=2, c=3)
# print(r1) # {'a': 1, 'b': 2, 'c': 3}
#
# r2 = func()
# print(r2) # {}
#
# r3 = func(a='python')
# print(r3) # {'a': 'python'}
#
# def func(*args, **kwargs):
#     return args, kwargs
#
#
# r1 = func(1, 2, 3, 'abc', a=4, b=5, c=4)
# print(r1) # ((1, 2, 3, 'abc'), {'a': 4, 'b': 5, 'c': 4})
#
# pos_args, named_args = func(1, 2, 3, 'abc', a=4, b=5, c=6)
# print(pos_args) # (1, 2, 3, 'abc')
# print(named_args) # {'a': 4, 'b': 5, 'c': 6}


# иногда бывает, что не хочется писать функцию ради какого-то действия
# в питоне для этого существуют функции без названия или анонимные функции

# func_a = lambda x, y: x + y # принимает на вход x, y. x + y это то, что будет возвращено


# эквивалентные записи
# def func_b(x, y):
#     return x + y
#
#
# a = (lambda x, y: x + y)(1, 10) # сразу вызываем функцию, она существует только здесь
# b = func_b(1, 10)
# print(a) # 11
# print(b) # 11

# как передать в функцию результат выполнения другой функции


def func_a(x, y):
    return x + y


def func_b(x, y):
    return x + y


res = func_a(func_b(1, 2), func_b(3, 4))
print(res) # 10
