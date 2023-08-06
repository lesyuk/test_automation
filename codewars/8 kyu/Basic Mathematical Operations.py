"""
The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
"""


def basic_op(operator, value1, value2):
    match operator:
        case '+':
            return value1 + value2
        case '-':
            return value1 - value2
        case '*':
            return value1 * value2
        case '/':
            try:
                return value1 / value2
            except ZeroDivisionError:
                print('Division by zero not allowed')


print(basic_op('*', 5, 2))