"""
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""


def simple_multiplication(n) :
    return n * 9 if n % 2 else n * 8
    # another sulution
    # return n * (8 + n % 2)
