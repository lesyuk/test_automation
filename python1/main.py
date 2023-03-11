num = 1
num1 = '123'

del num1  # удаление объекта из памяти

# нейминг переменныхD
my_var = 111
vat_111_____ = 111

_var = 1
__var = 1

# у питона есть классная штука под названием распаковка
# распаковать можно любой итерируемый объект
lst1 = [1, 2, 3, 4, 5]
# я хочу каждый элемент моего списка присвоить в переменную a, b, c, d, e
a, b, c, d, e = lst1  # каждая из переменных получила свой элемент списка
print(a, b, c, d, e)  # 1 2 3 4 5 # в данном случае произошла автоматическая распаковка, все элементы списка
# присвоились в том порядке, в котором мы передали
di = {1: 1, 2: 2, 3: 3}
# мы хотим проитерироваться и сразу получить и ключ и значение
di.items()  # возвращает список из кортежей где каждый 1 элемент кортежа это ключ, каждый 2 значение
for k, v in di.items():  # на каждой итерации цикла вернется кортеж из двух элементво и с помощью распаковки в
    # k присвоится 1-е значение, в v 2-е значение
    print(k, v)
# 1 1
# 2 2
# 3 3


# мы хотим распечатать весь наш список  lst через запятую
print(str(lst1))  # [1, 2, 3, 4, 5] - это строка, не список
# мы можем распечатать каждый элемент списка
print(*lst1)  # 1 2 3 4 5 // эта строчка эквивалента строчке ниже
print(a, b, c, d, e)  # 1 2 3 4 5
print(*lst1, sep=', ')  # 1, 2, 3, 4, 5

# распаковка ключей
print(*di)  # 1 2 3

# распаковка словаря ** и зачем это
year = 1999
month = 12
day = 31
filename = f'{year}-{month}-{day}'
print(filename)  # 1999-12-31
date = {'year': 1999, 'month': 12, 'day': 31}
filename = '{year}-{month}-{day}'.format(**date)  # 1999-12-31
# эквивалентном этой записи является:
print('{year}-{month}-{day}'.format(year=1991, month=12, day=31))  # 1991-12-31
## конструкция ** превратила словарь в запись вида year=1991, month=12, day=31
## * по сути лист на наш итерируемый объект отдельным элементами, ** это распаковка двухуровневых объектов

# изврашение, лучше так не делать:
filename2 = f'{date["year"]}-{date["month"]}-{date["day"]}'  # двойные кавычкеи потому что сама строка уже в ''
print(filename2)  # 1999-12-31

# конструкции управления потоком: условия

# тип ничто, пустая переменная, в дальнейшем если вдруг мы будем с ней взаимодействовать
welcome_str = None
# ......
# welcome_str = "hello, system, this is Mary"

# if 'Nick' in welcome_str: # операция вложенности строки в подстроку в условии
#     print('This is Nick')
# elif 'Mary' in welcome_str:
#     print('This is Mary')
# else:
#     print("Unknown person")

# This is Nick

# когда мы будем работать со строчками и проверять строчки на что-то здесь важнный момент что придется объявить
# переменную и заполним мы ее потом
if welcome_str is None:
    welcome_str = 'Test'

# начиная с питона 3.8 у нас появилась новая конструкция когда мы можем немного по-другому присваивать переменным значения

a = [1, 2, 3, 4, 5]

# если длина этого списка > 3 то мы напечатаем что-то длинное и длну этого списка
# как это было до питон 3.8
# length = len(a)
# if length > 3:
#     print('LONG')
#     print(length) # 5

# альтернатива: мы можем не вычислять длину заранее, мы можем вычислить ее в самом теле условия
# if len(a) > 3:
#     print('LONG')
#     print(len(a)) # 5

# в 3.8 появилась классная штука как walrus ператор. это лучший вариант = меньше строчек и вызовов длины
if (length := len(a)) > 3:  # в рантайме присваиваем переменной значение длины списка. len(a) выполняется 1 раз
    print('LONG')
    print(length)

# := еще называется моржовый оператор


var = 456

if var == 123:
    print('123')
elif var == 456:
    print('456')
else:
    print('don\'t know')

# начиная с питона 3.10 появились матчкейсы

# конструкции полностью эквиваленты,  но матчкейс - более читаемо и наглядно
# по скорости матч наверное будет быстрее чем операции if
match var:
    case 123:
        print('123')
    case 456:
        print('456')
    case _:
        print('don\'t know')


