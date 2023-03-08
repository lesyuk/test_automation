# Дана функция, которая ничего не делает случайное количество времени. Необходимо написать декоратор, который
# считает и выводит на экран время выполнения данной фукнкции.
import random
import time


def execution_time(f):
    def wrapper():
        start_time = time.time()
        f()
        print(f'Func execution time: {time.time() - start_time} sec')
    return wrapper


@execution_time
def func():
    time.sleep(random.randint(0, 10))


func()
func()
func()
