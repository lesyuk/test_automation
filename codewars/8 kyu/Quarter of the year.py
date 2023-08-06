"""
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month
11 (November), is part of the fourth quarter.
"""
from math import ceil


def quarter_of(month):
    return 1 if month / 3 <= 1 else 2 if month / 3 <= 2 else 3 if month / 3 <= 3 else 4

    # another solution
    # return ceil(month / 3)

    # another solution
    # return (month + 2) // 3


print(quarter_of(12))
