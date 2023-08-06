"""
When provided with a letter, return its position in the alphabet.
"""


def position(alphabet):
    return f'Position of alphabet: {ord(alphabet) - 96}'


print(position('z'))