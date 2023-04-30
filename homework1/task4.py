# Дан произвольный список. Необходимо написать минимум 4 способа развернуть данный список в обратную сторону.

# Один из способов должен быть реализован самостоятельно, без использования встроенных возможностей списка.

# 1st solution
some_list = [1, 4, 6, 9, 2, 3, 5]

some_list.reverse()

print(f'1st solution: {some_list}') # [5, 3, 2, 9, 6, 4, 1]

# 2nd solution

some_list = [1, 4, 6, 9, 2, 3, 5]

some_list = list(reversed(some_list))

print(f'2nd solution: {some_list}')

# 3rd solution

some_list = [1, 4, 6, 9, 2, 3, 5]

some_list = some_list[::-1]

print(f'3rd solution: {some_list}')

# 4th solution (own implementation)

some_list = [1, 4, 6, 9, 2, 3, 5]
new_list = []

for n in some_list:
    i = -abs(some_list.index(n) + 1)
    new_list.insert(i, n)

print(f'4th solution: {new_list}')

# ---

# 5th solution

some_list = [1, 4, 6, 9, 2, 3, 5]
new_list = []

for i in some_list:
    new_list.insert(0, i)

print(f'5th solution: {new_list}')

# 6th solution

some_list = [1, 4, 6, 9, 2, 3, 5]

for i in range(len(some_list)):
    some_list.insert(i, some_list.pop())

print(f'6th solution: {some_list}')

# 7th solution (best, like python work)

some_list = [1, 4, 6, 9, 2, 3, 5]

# do not create a new list and iterate over half of the list
for i in range(len(some_list) // 2):
    some_list[i], some_list[len(some_list) - 1 - i] = some_list[len(some_list) - 1 - i], some_list[i]

print(f'7th solution: {some_list}')

# 8th solution

some_list = [1, 4, 6, 9, 2, 3, 5]
new_list = [some_list[i] for i in range(len(some_list) - 1, -1, -1)]

print(f'8th solution: {new_list}')