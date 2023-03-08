# Написать контекстный менеджер, который принимает имя. При входе в контекст печатается приветствие по переданному
# имени. В тело контекста должно вернуться переданное имя в верхнем регистре.

# В теле контекста необходимо распечатать каждую букву верхнувшегося в верхнем регистре имени 3 раза.

# При выходе из контекста — печатается прощание по переданному имени.

# Задание необходимо реализовать двумя способами: с помощью класса и без.



# Реализация через класс


class NameTransformer:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Привет, {self.name}')
        return self.name.upper()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Пока, {self.name}')


context = NameTransformer('Павел')

with context as c:
    for letter in c:
        print(letter * 3)


# Реализация через функцию


from contextlib import contextmanager


@contextmanager
def context(name):
    print(f'Привет, {name}')

    yield name.upper()

    print(f'Пока, {name}')


with context('Pavel') as c:
    for letter in c:
        print(letter * 3)
