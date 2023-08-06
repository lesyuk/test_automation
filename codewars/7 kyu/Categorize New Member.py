"""
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an
application form that will tell prospective members which category they will be placed.
"""


def open_or_senior(data):
    # my solution using cycle
    # result = []
    # for k, v in data:
    #     if k >= 55 and v > 7:
    #         result.append('Senior')
    #     else:
    #         result.append('Open')
    # return result

    # my solution using list comprehension
    return ['Senior' if k >= 55 and v > 7 else 'Open' for k, v in data]


print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))
