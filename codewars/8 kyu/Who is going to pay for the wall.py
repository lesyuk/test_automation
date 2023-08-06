"""
Your code will show Full name of the neighbor and the truncated version of the name as an array. If the number of the
characters in name is less than or equal to two, it will return an array containing only the name as is
"""


def who_is_paying(name):
    return [name, name[:2]] if len(name) > 2 else [name]

# Через лямбду
# who_is_paying = lambda n: [n, n[:2]] if len(n) > 2 else [n]


print(who_is_paying("Dan"))
