"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument
(also a string).
"""


def solution(text, ending):
    return text[-len(ending):] == ending


print(solution('abc', ''))
