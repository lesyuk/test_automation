num_list = [1, 2, 3, 4, 5]

# в момент for i in создается итератор
# for i in num_list:
#     print(i)
#     # если ловим StopIteration то цикл завершен
#
#
# itr = iter(num_list)
#
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr)) # выходи за границы -  StopIteration. объект закончился


# на самом деле это больше генератор, потому что хранит состояние в counter
class SimpleIterator:

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    # объект становится итератором
    def __iter__(self):
        return self

    # позволяет по нему итерироваться
    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

s_iter = SimpleIterator(5)
# print(s_iter.counter)

for i in s_iter: # в i возвращается return self.counter
    print(i)

print(s_iter.counter) # 5