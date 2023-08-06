"""
Given the triangle of consecutive odd numbers:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
"""


def row_sum_odd_numbers(n):
    formula = n ** 2 - 2 * (n // 2) if n % 2 else (n - 1) ** 2 + 2 * (n // 2)
    return sum([formula + x for x in range(0, n * 2, 2)])


print(row_sum_odd_numbers(41))
