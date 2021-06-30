# Задание 1
# Python 3.9
# Windows 10 64bit

import sys


x1 = float(input('Введите координаты первой точки x1 '))
y1 = float(input('Введите координаты первой точки y1 '))
x2 = float(input('Введите координаты первой точки x2 '))
y2 = float(input('Введите координаты первой точки y2 '))
if x1 != x2:
    k = (y2 - y1) / (x2 - x1)
    b = y2 - k * x2
    print(f'Уравнение прямой y = {k:.2f}x + {b:.2f}')
else:
    print(f'Уравнение прямой x = {x1:.2f}')

my_sum = 0
my_list = (x1, y1, x2, y2, k, b)
for i in my_list:
    my_sum += sys.getsizeof(i)
print(f'Задействовано {my_sum} байт(а) памяти')
print(sys.getsizeof(x1))
print(sys.getsizeof(y1))
print(sys.getsizeof(x2))
print(sys.getsizeof(y2))
print(sys.getsizeof(k))
print(sys.getsizeof(b))
