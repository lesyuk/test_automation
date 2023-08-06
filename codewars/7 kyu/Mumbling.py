"""
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""


def accum(s):
    # return '-'.join(f"{s[i] * (i + 1)}".capitalize() for i in range(len(s)))

    # another solution
    # return '-'.join((c * i).capitalize() for i, c in enumerate(s, 1))

    # more CPU faster solution with building string
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))



print(accum('ZpglnRxqenU'))

print(dict(enumerate('ZpglnRxqenU')))