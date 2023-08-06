def remove_every_other(my_list):
    return [my_list[i] for i in range(len(my_list)) if not i % 2]

    # я тупой
    # return my_list[::2]


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))

# print(dict(enumerate(['Hello', 'Goodbye', 'Hello Again'])))
