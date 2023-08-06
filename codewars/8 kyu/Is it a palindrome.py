"""
Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards,
such as madam or racecar, the date and time 12/21/33 12:21, and the sentence: "A man, a plan, a canal – Panama".
"""


def is_palindrome(s):
    return s.lower() == s[::-1].lower()


print(is_palindrome('Abbb'))
