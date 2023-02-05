# Напишите функцию, которая при заданном целом числе n складывает цифры этого числа и выводит результат.

def print_sum(n):
    converted_n = str(n)
    sum_n = 0
    for i in converted_n:
        sum_n += int(i)
    return sum_n


user_input = print_sum(input('Enter number: '))
print(user_input)
