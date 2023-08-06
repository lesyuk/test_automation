# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python


def printer_error(s):
    # return f'{[ch in "abcdefghijklm" for ch in s].count(False)}/{len(s)}'

    # another solution
    # return f"{len([x for x in s if x not in 'abcdefghijklm'])}/{len(s)}"

    # ideomatic solution
    return f'{sum(x > "m" for x in s)}/{len(s)}'

    # another solution
    # errors = sum(not("a" <= c <= "m") for c in s)
    # return f"{errors}/{len(s)}"


print(printer_error('kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu'))
