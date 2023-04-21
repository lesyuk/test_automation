"""
Homework description:

Напишите функцию, которая при заданном целом числе n складывает цифры этого числа и выводит результат.
"""

from functools import reduce


# str arg (own solution)
def print_str_sum(n):
    sum_n = 0
    for i in n:
        try:
            sum_n += int(i)
        except ValueError:
            print('Unexpected argument')
            break
    if sum_n:
        print(sum_n)


print_str_sum(input('Enter number: '))


# int arg without convert to str (best math solution)
def print_int_sum(n):
    summa = 0
    while n != 0:
        summa += n % 10 # addition of the remainder of a division to summa (example 11 % 10 = 1)
        n //= 10 #
    print(summa)


print_int_sum(1234567890)


# int arg convert to string (using map)
def print_int_to_str_sum(n):
    # int is a function, which maps on the every symbol of str and creates a list of them
    print(sum(map(int, str(n))))


print_int_to_str_sum(1234567890)


# int arg convert to string (using reduce)
def print_int_to_str_sum2(n):
    summa = reduce(lambda x, y: int(x) + int(y), str(n))
    print(summa)


print_int_to_str_sum2(1234567890)
