# Дан произвольный список. Необходимо написать минимум 4 способа развернуть данный список в обратную сторону.

# Один из способов должен быть реализован самостоятельно, без использования встроенных возможностей списка.

# First way
some_list = [1, 4, 6, 9, 2, 3, 5]

some_list.reverse()

print(some_list) # [5, 3, 2, 9, 6, 4, 1]

# Second way

some_list = [1, 4, 6, 9, 2, 3, 5]

some_list = list(reversed(some_list))

print(some_list)

# Third way

some_list = [1, 4, 6, 9, 2, 3, 5]

some_list = some_list[::-1]

print(some_list)

# Fourth way (own implementation)

some_list = [1, 4, 6, 9, 2, 3, 5]
new_list = []

for n in some_list:
    i = -abs(some_list.index(n) + 1)
    new_list.insert(i, n)

print(new_list)
