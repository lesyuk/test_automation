"""
In this kata you will create a function that takes in a list and returns a list with the reverse order.
"""


def reverse_list(l):
    # return l[::-1]

    # another solution
    # return list(reversed(l))

    # another solution
    # l.reverse()
    # return l

    # how it works under the hood
    for i in range(len(l) // 2):
        l[i], l[len(l) - 1 - i] = l[len(l) - 1 - i], l[i]
    return l


print(reverse_list([1, 2, 3, 4]))
