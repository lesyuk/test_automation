"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's
divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string
'(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>,
String> in Rust).
"""


def divisors(integer):
    # divisors_list = [d for d in range(2, integer // 2 + 1) if integer % d == 0]
    # return divisors_list if divisors_list else f'{integer} is prime'

    # another way to return all with 1 string using OR
    return [d for d in range(2, integer // 2 + 1) if integer % d == 0] or f'{integer} is prime'


print(divisors(24))

# from math import sqrt, floor
#
# def divisors(integer):
#     def find_divisor_partner(n):
#         return integer / n
#
#     cap = int(floor(sqrt(integer)))
#     is_perfect_sq = cap ** 2 == integer
#     cap = cap if is_perfect_sq else cap + 1
#     divisors = [cap] if is_perfect_sq else []
#
#     for i in xrange(2, cap):
#         if integer % i == 0:
#             divisors.extend([i, find_divisor_partner(i)])
#
#     divisors.sort()
#     return divisors if divisors else '{} is prime'.format(integer)

# def divisors(integer):
#     small_divs, large_divs = [], []
#     for n in range(2,int(integer**0.5)+1):
#         if integer%n == 0:
#             small_divs.append(n)
#             if n**2 != integer:
#                 large_divs.append(integer//n)
#     divs = small_divs + list(reversed(large_divs))
#     return divs if divs else '{} is prime'.format(integer)
