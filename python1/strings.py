my_str = '123456'

my_str += '6'
#
my_str = my_str + '6' # результирующее значение переприсвоится в my_str (новый объект). изначальная ссылка будет удалена gc

# двойные кавычки тоже можно
my_str1 = "1234"

# тройные кавычки позволяют делать мультилайн
my_str2 = """
123123
adasdasdas
asdasdasdasd
"""

# спецсимволы

my_str3 = '123\n456'
print(my_str3)
# 123
# 456

# если нужно напечатать символ как есть
my_str3 = r'123\n456' # r - raw (сырая)
print(my_str3) # 123\n456

string = 'hello world'
splitted = string.split(' ')

for i in 'hello':
    print(i)

for i in 'hello':
    print(i, end='') # hello

print()
# форматирование строк
a = '1'
b = '2'
c = '3'

# вариант как в C
string = 'This is a <%s>, this is b <%s>, this is c <%s>' % (a, b, c)
print(string) # This is a <1>, this is b <2>, this is c <3>

# более удобный через format()
string1 = 'This is a <{}>, this is b <{}>, this is c <{}>'.format(a, b, c)
print(string1) # This is a <1>, this is b <2>, this is c <3>

# самый удобный. является форматом де-факто, они быстрее чем формат штатный и чем %. используем его всегда
string2 = f'This is a <{a}>, this is b <{b}>, this is c <{c}>'
print(string2) # This is a <1>, this is b <2>, this is c <3>

