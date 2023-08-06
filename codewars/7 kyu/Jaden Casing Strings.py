"""
Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from
Jaden Smith, but they are not capitalized in the same way he originally typed them.
"""


def to_jaden_case(string):
    return ' '.join(w.capitalize() for w in string.split())


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
