"""
Write a function that returns both the minimum and maximum number of the given list/array.
"""


def min_max(lst):
    mn, mx = lst[0], lst[0]
    for num in lst:
        if num < mn:
            mn = num
        elif num > mx:
            mx = num
    return [mn, mx] if mn != mx else [mn]
    # return [min(lst), max(lst)]

print(min_max([]))