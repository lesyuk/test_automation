"""
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built
with the sides of given length and false in any other case.
"""


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

    # math solution
    # return 2 * max(a, b, c) < a + b + c

    # another math solution
    # a, b, c = sorted([a, b, c])
    # return a + b > c

    # another
    # return abs(a-b) < c < a+b


print(is_triangle(1, 2, 2))