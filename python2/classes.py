# class Human:
#     # описание объекта (схема)
#     age = None
#     sex = None
#     weight = None
#
#     # методы с __ называются магическими
#     # переопределением встроенного метода класса, который обращается к атрибуту инстанса
#     # self - ссылка на инстанс (обязательный аргумент у функции класса, работает только в рантайме, когда создан
#     # экземпляр, в данном случае human1
#     # item - переданный age
#     def __getattribute__(self, item):
#         print(f'Now i will return {item} of {self}')
#
#     # сет атрибутов
#     # key = age, sex, weight
#     # value = переданное значение
#     def __setattr__(self, key, value):
#         print(f'Now i will set {key}={value} of {self}')
#
#     # удаление из конкретного инстанса конкретный атрибут
#     def __delattr__(self, item):
#         print(f'I will delete {item} of {self}')
#
#
# # lst = [1, 2, 3]
# # lst.remove() # у объекта класса list есть метод remove
#
# human1 = Human() # из схемы создаем объект (инстанс класса, экземпляр), который обладает свойствами класса Human
# print(human1)
# # Now i will return age of <__main__.Human object at 0x100ede0d0>
# print(human1.age) # . это обращение к атрибуту / свойству / функции объекта
#
# human2 = Human()
# print(human2)
#
# # setattr
# human1.age = 20
# human1.sex = 'M'
# human1.weight = 80
#
# human2.age = 18
# human2.sex = 'F'
# human2.weight = 50
#
# del human2.age
#
# # посмотреть все атрибуты объекта (надо закомментить принты маг методов в классе)
# print(human1.__dict__) # {'age': 20, 'sex': 'M', 'weight': 80}
# print(human2.__dict__) # {'sex': 'F', 'weight': 50}

class Human:
    _age = None # инкапсуляция. приватные переменные не наследуются (через __)

    # сеттер инстанса
    def set_age(self, age):
        self._age = age

    # геттер инстанса
    def get_age(self):
        return self._age

# human = Human()
# print(human.__age) # 'Human' object has no attribute '__age' - приватная переменная
# print(human.get_age())
# human.set_age(18)
# print(human.get_age())

# наследование
class Man(Human):
    pass

class Woman(Human):

    # переопределяем get_age
    @property # можно не вызывать функцию через (), а обращаться как к атрибуту через .get_age
    def get_age(self):
        return self._age - 10


man = Man()
man.set_age(60)
print(man.get_age())

woman = Woman()
woman.set_age(30)
print(woman.get_age)

# проверка: подкласс класса
print(issubclass(Woman, Human))
# проверка: инстанс класса
print(isinstance(woman, Human))

# все аттрибуты конкретного объекта
print(dir(Woman))
