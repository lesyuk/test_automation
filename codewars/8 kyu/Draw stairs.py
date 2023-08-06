def draw_stairs(n):
    some_s = """"""
    for i in range(1, n + 1):
        if i != n:
            some_s += 'I\n' + ' ' * i
        else:
            some_s += 'I'
    print(some_s)


draw_stairs(3)