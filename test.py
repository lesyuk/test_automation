def multiply(n):
    str_n = str(n)
    degree = 0
    if str_n[0] != '-':
        degree = len(str_n)
    else:
        degree = len(str_n) - 1
    return n * 5 ** degree

print(multiply(100))
print(multiply(-100))

## best practice

def multiply2(n):
    return n * 5 ** len(str(abs(n)))

print(multiply2(-100))