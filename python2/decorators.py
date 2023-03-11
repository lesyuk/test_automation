# Проблема: есть функция, ничего не делает.
# Я хочу считать, сколько раз была вызвана эта функция на протяжении моей программы.
# На помощь приходит паттерн программирования — декоратор.
# Декоратор — это функция, которая принимает на вход другую функцию.
# Похоже на функцию высшего порядка.
from functools import wraps

counter = {} # {'func': 3, 'func1': 2}


# Декоратор — функция, которая возвращает функцию.
def count_decorator(f):
    @wraps(f) # возвращает изначальные значения фукнции (название, docstring и пр)
    def wrapper(*args, **kwargs): # главенствует над func
        name = f.__name__
        if name in counter:
            counter[name] += 1
        else:
            counter[name] = 1
        return f(*args, **kwargs)
        # обязательно return, если хотим, чтобы работало правильно
    # func() missing 1 required positional argument: 'x'
    return wrapper



@count_decorator # метим декоратором. эквивалентно decorator = count_decorator(func). декоратор должен быть написан перед меткой
def func(x, y=6):
    # global counter
    # counter += 1
    return x * y

def_1 = func(2)
print(def_1)


print(func.__name__) # wrapper - обращаемся к нему. это бывает проблемой. решает через @wraps


# @count_decorator
def func1(x):
    print(x)


print(func1.__name__)


# r1 = func(1, 2) # count_decorator.<locals>.wrapper() takes 0 positional arguments but 1 was given если wrapper() без аргументов
# r2 = func(2, y=3)
# r3 = func(3)
#
# func1('123')
# func1('456')
#
#
# print(r1, r2, r3) # None None None
#
# print(counter)


# Декоратор не только меняет поведение функции, но и меняет кое-что другое.


