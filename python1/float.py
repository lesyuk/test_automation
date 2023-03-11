from decimal import Decimal

float_num = 3.14
float_num1 = 3.14e2 # 3.14 * 100 (10 во сторой степени)

print(type(float_num)) # <class 'float'>

# 3.14 не является этим числом для компа, у числе с . есть величина приближения
print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1) # 0.9999999999999999


precise_float = Decimal('0.111111111111') # если передать число строкой, то остается именно то значение, которое мы использем
print(precise_float) # 0.111111111111

print(int(float_num)) # 3. округление (преобразование) в питоне всегда работает в меньшую сторону
