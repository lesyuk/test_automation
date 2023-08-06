"""
Given an array of integers, remove the smallest value. Do not mutate the original array/list.
If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list,
return an empty array/list.

Don't change the order of the elements that are left.
"""


def remove_smallest(numbers):
    if not numbers:
        return []
    numbers_copy = numbers.copy()
    numbers_copy.remove(min(numbers_copy))
    return numbers_copy


lst = [2, 2, 1, 2, 1]

print(remove_smallest(lst))
print(lst)
