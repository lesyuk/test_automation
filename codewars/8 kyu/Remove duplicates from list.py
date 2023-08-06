def distinct(seq):
    return list({}.fromkeys(seq))


print(distinct([5, 5, 4, 4, 3, 3, 2]))