"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""
from functools import reduce


def find_short(s):
    return len(min(s.split(), key=len))

    # another solution
    # return min(map(len,s.split()))

    # another solution
    # return min(len(x) for x in s.split())


print(find_short())
