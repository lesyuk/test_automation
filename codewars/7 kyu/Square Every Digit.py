"""
In this kata, you are asked to square every digit of a number and concatenate them.
Note: The function accepts an integer and returns an integer.
"""


def square_digits(num):
    # my solution #1
    # sm = '0'
    # while num:
    #     sm += str((num % 10) ** 2)
    #     num //= 10
    # return int(sm)

    # my solution #2
    return int(''.join(str(int(x) ** 2) for x in str(num)))


print(square_digits(9119))
