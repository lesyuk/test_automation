"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest
number.

There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""


def high_and_low(numbers):
    """
    For long input, this implementation is slow because max and min has to traverse list twice. It's possible to optimize
    that by iterating over the list once, and finding max & min value along that one iteration. For example, see @schp
    solution (using reduce)
    """
    # numbers = list(map(int, numbers.split(' ')))
    # return f'{max(numbers)} {min(numbers)}'

    # another solution
    # return " ".join(x(numbers.split(), key=int) for x in (max, min))

    # trying reduce() (2 iterations)
    from functools import reduce
    return f'{reduce(max, numbers.split(" "))} {reduce(min, numbers.split(" "))}'





print(high_and_low('1 2 3 4 5'))
