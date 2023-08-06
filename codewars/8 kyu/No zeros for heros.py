"""
Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.
"""


def no_boring_zeros(n):
    while not n % 10 and n:
        n /= 10
    return n

    # another solution
    # return int(str(n).strip("0")) if n else n


print(no_boring_zeros(2016))
