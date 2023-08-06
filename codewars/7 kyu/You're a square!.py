"""
Given an integral number, determine if it's a square number:
"""
import math


def is_square(n):
    return False if n < 0 else n == math.sqrt(n) * math.sqrt(n)

    # another solution
    # return n > -1 and (n ** 0.5) % 1 == 0


print(is_square(24))