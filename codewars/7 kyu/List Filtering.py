"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list
with the strings filtered out.
"""


def filter_list(l):
    return [x for x in l if type(x) is int]


print(filter_list([1, 2, 'aasf', '1', '123', 123]))
