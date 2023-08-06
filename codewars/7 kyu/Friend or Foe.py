"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure
he's not...
"""


def friend(x):
    return [s for s in x if len(s) == 4]


print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]))
