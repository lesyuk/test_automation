"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
return the middle character. If the word's length is even, return the middle 2 characters.
"""


def get_middle(s):
    len_s = len(s)
    return s[len_s // 2] if len_s % 2 else s[len_s // 2 - 1:len_s // 2 + 1]

    # index, odd = divmod(len(s), 2)
    # return s[index] if odd else s[index - 1:index + 1]

    # genius
    #  i = (len(s) - 1) // 2
    #     return s[i:-i] or s

    # another
    # while len(s) > 2:
    #         s = s[1:-1]
    #     return s


print(get_middle('1'))