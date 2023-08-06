"""
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
"""


def find_next_square(sq):
    x = sq ** .5
    return -1 if x % 1 else (x + 1) ** 2


print(int(626**0.5)**2)
