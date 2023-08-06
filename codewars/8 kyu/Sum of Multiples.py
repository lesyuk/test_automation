# Find the sum of all multiples of n below m

def sum_mul(n, m):
    return 'INVALID' if m < 1 or n < 1 else sum(i * n for i in range((m - 1) // n + 1))
    # Алгоритм
    # if m < 0:
    #     return 'INVALID'
    # iters = (m - 1) // n
    # sm = 0
    # for i in range(iters + 1):
    #     sm += n * i
    # return sm

    # Самое короткое
    # return sum(range(n, m, n)) if n > 0 < m else 'INVALID'


print(sum_mul(0, 0))