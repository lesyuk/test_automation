# Написать бесконечно работающий калькулятор.
#
# Детали реализации:
# 1. Пользователю предлагается выбрать действие (список действий предварительно выводится на экран)
# * ввод "1" - сложение (+)
# * ввод "2" - вычитание (-)
# * ввод "3" - умножение (*)
# * ввод "4" - деление (/)
#
# 2. Если пользователь выбирает недопустимое действие — выводится ошибка и пользователю предлагается выбрать действие
# повторно
#
# 3. Если выбрано существующее действие, пользователю предлагается ввести сначала первое число, затем второе
#
# 4. Если пользователем вводится не число хотя бы в одной из двух значений - выдается ошибка и программа возвращается к п.1
#
# 5. Если введены корректные числа - выполняем действие, выводим результат на экран и переходим к п. 1

def check_user_input(user_input):
    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        try:
            user_input = float(user_input)
            return user_input
        except ValueError:
            print('The entered value is not a number. Please, try again.')
            return ValueError


while True:
    print('Choose an action from the list below:\n'
          '1 - addition (+)\n'
          '2 - subtraction (-)\n'
          '3 - multiplication (*)\n'
          '4 - division (/)\n')
    while True:
        operation = input('Enter the code of the action: ')
        match operation:
            case '1':
                break
            case '2':
                break
            case '3':
                break
            case '4':
                break
            case _:
                print('Incorrect input. Please, try again.')
                continue

    first_num = check_user_input(input('Enter the first number: '))
    if first_num is ValueError:
        continue
    second_num = check_user_input(input('Enter the second number: '))
    if second_num is ValueError:
        continue
    match operation:
        case '1':
            print(f'Calculation result: {first_num + second_num}')
        case '2':
            print(f'Calculation result: {first_num - second_num}')
        case '3':
            print(f'Calculation result: {first_num * second_num}')
        case '4':
            try:
                print(f'Calculation result: {first_num / second_num}')
            except ZeroDivisionError:
                print('Dividing by zero is undefined.')
