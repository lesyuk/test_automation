"""
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
"""


def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

l = [1, 2, 3, 4, 5, 6, 7, 8, 5]
# print(*l)
print(find_average(l))
