# Напишите функцию, которая при заданном целом числе n складывает цифры этого числа и выводит результат.

def print_sum(n):
    sum_n = 0
    for i in n:
        try:
            sum_n += int(i)
        except ValueError:
            print('Unexpected argument')
            exit()
    print(sum_n)

user_input = print_sum(input('Enter number: '))
