"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(sentence):
    return sum(map(sentence.count, 'aeiou'))

    # another solution
    # sum(c in 'aeiou' for c in s)


print(get_count("aeiou"))