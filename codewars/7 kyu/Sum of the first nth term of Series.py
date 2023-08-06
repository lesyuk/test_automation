"""
Your task is to write a function which returns the sum of following series upto nth term(parameter).

1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
"""


def series_sum(n):
    if n <= 1:
        return n

    total = 1
    for x in range(3, n * 2 + 1, 3):
        total += 1 / (4 + x)

    return total
    # return n if n <= 1 else 1 + 1 / (4 + 3 * (n - 2))


print(series_sum(2))