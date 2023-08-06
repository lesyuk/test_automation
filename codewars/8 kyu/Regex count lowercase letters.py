def lowercase_count(strng):
    lc = 0;
    for l in strng:
        if l.islower():
            lc += 1
    return lc


st = 'abcABC123'
print(lowercase_count(st))