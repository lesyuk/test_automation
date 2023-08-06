my_str = '1234566666' # ссылка на '12345'

my_str += '6'
# эквивалентно
# результирующее значение переприсвоится в my_str (новый объект). Изначальная ссылка будет удалена gc
my_str = my_str + '6'

# двойные кавычки тоже можно
my_str1 = "1234"

# тройные кавычки позволяют делать мультилайн
my_str2 = """
123123
adasdasdas
asdasdasdasd
"""

print(my_str2)

# спецсимволы
my_str3 = '123\n456'
print(my_str3)
# 123
# 456

# если нужно напечатать символ как есть
my_str3 = r'123\n456' # r - raw (сырая)
print(my_str3) # 123\n456

# строки можно складывать
print('123' + '' + '456')

# строчки напоминают списки, это массив char'ов под капотом CPython

# можем обратиться к индексу
print('hello'[0])

# можем посмотреть длину последовательности
print(len('hello' * 3))

# методы строки
# посчитать количество значений в строке
print(my_str.count('6'))
# строчка с большой буквы
my_str = 'hello'.capitalize()
print(my_str)
# проверить является ли строка числом
print('123456'.isdigit())
# проверить все ли символы в нижнем регистре
print('qwezxC'.islower())
# количество заране подготовленных методов есть практически во всех типах
# сплит строки по пробелу
string = 'hello world'
splitted = string.split(' ')
print(splitted)
# содержит ли одна строка другую или нет
print('hello' in 'hello world')
# сравнение строк регистрозависимое
print('hello' == 'Hello')
# если мы хотим сравнивать две строчки и забить на регистр, то нужно вызывать lower на строках (или upper)
# с вхождением подстроки в строку тоже самое
print('hello'.lower() == 'Hello'.lower())


for i in 'hello':
    print(i) # h/ne/nl/nl/no

for i in 'hello':
    print(i, end='') # hello

print()
print
# форматирование строк (сборка строк из разных частей)
a = '1'
b = '2'
c = '3'
# Форматирование несколькими способами
# вариант как в C
string = 'This is a <%s>, this is b <%s>, this is c <%s>' % (a, b, c)
print(string) # This is a <1>, this is b <2>, this is c <3>

# более удобный через format()
string1 = 'This is a <{}>, this is b <{}>, this is c <{}>'.format(a, b, c)
print(string1) # This is a <1>, this is b <2>, this is c <3>

# самый удобный. является форматом де-факто, они быстрее чем формат штатный и чем %. используем его всегда
string2 = f'This is a <{a}>, this is b <{b}>, this is c <{c}>'
print(string2) # This is a <1>, this is b <2>, this is c <3>

# любая пустая строчка это false
print('Пустая строка равна ' + str(bool('')))

# любая не пустая строчка это true
print('Не пустая строка равна ' + str(bool('qwe')))
