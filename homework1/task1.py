"""
Homework description:

Дан некоторый список чисел.
Необходимо написать код, который последовательно выводит нечетные числа данного списка, а встретив
число 666 - останавливает вывод.
Если мы встречаем число 666 повторно - снова начинаем вывод, но уже четных чисел.
И так далее.
"""

nums = [849, 200, 809, 164, 926, 84, 892, # print odds: 849, 809
        666,
        880, 869, 775, 707, 874, 195, 120, 275, 328, 228, 43, 445, 421, 246, # not print
        666,
        324, 107, 455, 632, # print evens: 324, 632
        666,
        468, 603, 500, # not print
        666,
        123, 435, 888, # print odds: 123, 435
        666,
        1, 1, 1, 1, 1, 2, 2, 2, 2, # not print
        666,
        2, 2, 4, 3] # print evens: 2, 2, 4

# Own solution

"""
flag values:
1 - odd
2 - not print
3 - even
4 - not print
"""

flag = 1

for i in nums:
    match flag:
        case 1:
            if i != 666:
                if i % 2 != 0:
                    print(i)
            else:
                flag = 2
        case 2:
            if i == 666:
                flag = 3
        case 3:
            if i != 666:
                if i % 2 == 0:
                    print(i)
            else:
                flag = 4
        case 4:
            if i == 666:
                flag = 1

# Logic solution

make_print = True
modulo = True

for i in nums:
    if i == 666:
        make_print = not make_print
        if make_print: # using the walrus operator: if make_print := not make_print
            modulo = not modulo
    elif make_print and i % 2 == modulo:
        print(i)

# Math solution

cnt = 0

for num in nums:
    if num == 666:
        cnt += 1
        continue
    if cnt % 2 != 0: # Whether to print or not. True if cnt even
        continue
    elif (cnt / 2) % 2 == 0: # Print odd. Every 2 numbers of cnt / 2 will be even
        if num % 2 != 0:
            print(num)
    elif (cnt / 2) % 2 != 0: # Print even. Every 2 numbers of cnt / 2 will be odd
        if num % 2 == 0:
            print(num)
