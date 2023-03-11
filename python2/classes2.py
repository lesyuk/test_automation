class PlanetClass:
    count = 0                   # атрибут класса. в момент инита все классовые атрибуты так же становятся атрибутами
                                # экземпляра и с ними можно что-то делать

    def __init__(self, name):   # конструктор
        self.name = name        # атрибут экземпляра

    def __repr__(self):
        return f'Name: "{self.name}"\nCount: {self.count}'

    def __int__(self):
        return self.count

    def __str__(self):
        return f'Счетчик: {self.count}'


planet_1 = PlanetClass('Земля') # создаем экземпляр класса
planet_1.count += 1             # инкрементируем атрибут экземпляра "земля"

PlanetClass.count += 2          # глобально инкрементируем атрибут класса

planet_2 = PlanetClass('Марс')  # создаем экземпляр класса. здесь count уже равен 2
planet_2.count += 1             # инкрементируем атрибут экземляра "марс"


# print(planet_1.count)
# print(planet_2.count)
#
# print(planet_2.name)
print(planet_2) # <__main__.PlanetClass object at 0x10aa75b10>. Можно поменять через __repr__
print(int(planet_1.count)) # __int__
print(str(planet_1))