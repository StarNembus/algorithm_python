# Задание 1
# Алгоритм нахождения суммы цифр трехзначного числа abc (где a - сотни, b - десятки и c - единицы):
# Найти остаток от деления abc на 10, записать его в переменную d1. Это будет цифра c.
# Избавиться от цифры c в числе abc, разделив его нацело на 10.
# Найти остаток от деления ab на 10, записать его в переменную d2. Это будет цифра b.
# Избавиться от цифры b в числе ab, разделив его нацело на 10.
# Число a однозначное. Это еще одна цифра исходного числа.
# Сложить оставшееся число a со значениями переменных d1 и d2.#

n = input("Введите трехзначное число: ")
n = int(n)

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10

print("Сумма цифр числа:", n + d1 + d2)

# Задание 3

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

# Задание 4

from random import random

m1 = int(input())
m2 = int(input())
n = int(random() * (m2 - m1 + 1)) + m1
print(n)

m1 = float(input())
m2 = float(input())
n = random() * (m2 - m1) + m1
print(round(n, 3))

m1 = ord(input())
m2 = ord(input())
n = int(random() * (m2 - m1 + 1)) + m1
print(chr(n))

# Задание 5
a = ord(input('1-я буква: '))
b = ord(input('2-я буква: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print('Позиции: %d и %d' % (a, b))
print('Между буквами символов:', abs(a - b) - 1)

# Задание 6
n = int(input('Номер буквы в алфавите: '))
n = ord('a') + n - 1
print('Это буква', chr(n))

# Задание 7
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")

# Задание 8
y = int(input())
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print("Обычный")
else:
    print("Високосный")

# Задание 9
print('Введите три числа: ')
a = int(input())
b = int(input())
c = int(input())

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)




