"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive
integers. No floats or non-positive integers will be passed.
"""


def sum_two_smallest_numbers(numbers):
    # O(n log n)
    # return sum(sorted(numbers)[:2])

    # O(n)
    smallest1 = None
    smallest2 = None
    for n in numbers:
        if not smallest1 or n < smallest1:
            smallest2 = smallest1
            smallest1 = n
        elif not smallest2 or n < smallest2:
            smallest2 = n
    return smallest1 + smallest2


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
