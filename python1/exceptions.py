import traceback

# исключения будут возникать постоянно, это нормальная работа кода
# наша задача как программистов этими исключениями уметь пользоваться и не позволять чтобы они приводили к завершению
# как только возникает исключение и если оно никак не перехватывается наша  программа выдает ошибку и выходит

1 + 1
1 + 2

1 / 2

# потенциально если мы знаем что второе значение может быть равно 0 мы можем его обработать (захендлить)
try:
    1 / 0
except:
    print('Something bad happened') # программа не упала и продолжила работать

print('continue')

# перехватываем конкретное исключение ZeroDivisionError
try:
    1 / 0
except ZeroDivisionError: #
    print('Something bad happened') # программа не упала и продолжила работать


# программа все-равно падает, потому что возникшее исключение возникает раньше обработанного
# try:
#     1 + 'a'
#     1 / 0
# except TypeError:
#     print('Something bad happened') # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# у питона на все случаи жизни есть свои исключения: типа, значения, zerodivision, пустой индекс

# try:
#     [][0] # обращение к пустому списку
# except IndexError:
#     print('Something bad happened')

# простой пример: хотим заставить пользователя ввести два числа и попробовать поделить их друг на друга
# try:
#     a = int(input('Enter a: ')) # приводим к инту, так как вводится в строчном типе
#     b = int(input('Enter b: '))
# except ValueError:
#     print('Invalid enter')
#     exit()

# try:
#     print(a // b)  # целочисленное деление
# except ZeroDivisionError:
#     print('b is zero')
# print('continue')


# или другой вариант
# if b == 0:
#     exit() # выход скрипта
#
# print(a // b)

# проверка на дурака если a будет строкой ValueError: invalid literal for int() with base 10: 'фывфывфыв'

# исключения можно варьировать друг относительно друга (стакать)
try:
    a = int(input('Enter a: ')) # приводим к инту, так как вводится в строчном типе
    b = int(input('Enter b: '))
    print(a // b)
except ValueError:
    print('Invalid enter')
    exit(0)

except ZeroDivisionError as e: # as e - сохранить значение объекта экспепшена в переменную е
    print(e) # integer division or modulo by zero
    # если хотим прям совсем подробное описание эксепшена засейвить в переменную
    traceback.print_exc() # печатаем трасировку экспшен но программа не падает
    print('zero divison')
    # exit(0)

except: # хз как проверить на конкретном примере
    print('smth very bad')
    raise Exception() # raise - это нами в нашем управляемом коде наше выброшенное исключение
    # нужно

# по pep8 нельзя использовать bare except, то есть очень широкий except без указания конкретного, но это спорное правило

print('continue')

