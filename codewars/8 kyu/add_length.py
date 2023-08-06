# Your task is to write a function that takes a String and returns an Array/list with the length of each word
# added to each element.

def add_length(str_):
    return [x + (" " + str(len(x))) for x in str_.split()]

print(add_length("Sample Tests"))