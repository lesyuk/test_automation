"""
Your task is to write a function maskify, which changes all but the last four characters into '#'.
"""


def maskify(cc):
    # return cc if len(cc) < 4 else '#' * (len(cc) - 4) + cc[-4:]

    # shorter solution
    return '#' * (len(cc) - 4) + cc[-4:]


print(maskify('1'))
