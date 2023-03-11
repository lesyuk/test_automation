def simple_generator(val):
    while val > 0:
        val -= 1
        yield 1


gen_iter = simple_generator(5)

# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))


# на каждую итерацию генератор возвращает значение до тех пор пока не поймет что пора прекращать
# то есть это не готовый список [1,1,1,1,1]
# генератор будет в один момент всегда занимать число 1
# for i in gen_iter:
#     print(i)
#
# f = open('test', 'r') # 100 gb
# print(f.read())
# f.close()

# f — открытый файл (контекстный менеджер), а так же объект генератора
with open('test') as f:
    for line in f:
        print(line)
# при выходе из with автоматически дернется f.close()
