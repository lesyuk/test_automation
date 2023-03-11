# f = open('test', 'r') # путь и как мы открываем файл
# print(f.name) # имя файла
#
# print(f.readline()) # читаем строчку
# print(f.readline())
#
# print(f.tell()) # на какой строчке находимся
# f.close() # закрываем файл


# def read(path):
#     f = open(path, 'r')
#     try:
#         print(f.name)
#
#         print(f.readline())
#         print(f.readline())
#
#         print(f.tell())
#     finally:
#         f.close()


# read('test')


class FileOpener:

    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, 'r')
        print(self.file.name)
        return self

    def read(self):
        print(self.file.readline())

    def seek_to_start(self):
        self.file.seek(0) # возврат в начало файла

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.file.tell())
        self.file.close()


f_opener = FileOpener('test')
# с помощью чего-то сделать что-то
# в момент with вызываем __enter__
# return self попадет в as test_file
with f_opener as test_file: # as test_file - записываем результат в test_file
    test_file.read()
    test_file.read()
    test_file.read()
    test_file.seek_to_start()
    print(test_file.file.readline())
    # здесь вызывается __exit__


from contextlib import contextmanager


@contextmanager # помечая функцию этим декоратором, мы по сути превращаем функцию в подобие классы выше
def file_opener(file_path):
    # все, что до yield — это метод __enter__
    f = open(file_path, 'r')
    print(f.name)

    yield f # позволяет вернуть результат это функции тому кто ее вызывал, но потом вернуться и продолжить выполнение

    # все, что после yield — это метод __exit__
    print(f.tell())
    f.close()


with file_opener('test') as f:
    print(f.readline())
    print(f.readline())


# Когда нужно писать на классе а когда на функции
# если простой пример то функция
# если что-то хранить / менять, то класс (когда контекстный менеджер делает что-то +- сложное)

