"""
Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained.
"""


def reverse_words(text):
    return ' '.join(x[::-1] for x in text.split(' '))


print(reverse_words('double  spaced  words'))
