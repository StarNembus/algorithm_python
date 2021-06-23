# Задание 1
print("Ноль в качестве знака операции завершит работу программы")
while True:
    s = input("Какое действие необходимо выполнить, введите значение(+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x + y))
        elif s == '-':
            print("%.2f" % (x - y))
        elif s == '*':
            print("%.2f" % (x * y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x / y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")

# Задание 2

n = int(input('Введите число: '))
even = odd = 0
while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
print("четных - %d, нечетных - %d" % (even, odd))

# Задание 3

a = int(input('Введите число: '))
b = 0
while a > 0:
    b = b * 10 + a % 10
    a = a // 10
print(b)

# Задание 4
n = int(input('Введите число: '))
value = 1
amount = value


def recursion(n, value, amount):
    if n == 0:
        return 0
    if n == 1:
        return amount

    value = value / -2
    amount = amount + value
    n = n - 1
    return recursion(n, value, amount)


print(recursion(n, value, amount))


# Задание 5
for i in range(32, 128):
    print("%4d-%s" % (i, chr(i)), end='')
    if i % 10 == 0:
        print()
print()

# Задание 6

from random import random

n = round(random() * 100)
i = 1
print('Необходимо отгадать число, которое загадала система. У вас 10 попыток')
while i <= 10:
    x = int(input(str(i) + '-я попытка: '))
    if x > n:
        print('Меньше ')
    elif x < n:
        print('Больше ')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Число ', n)

# Задание 7
n = int(input('Введите число: '))
a = 0
for i in range(1, n + 1):
    a += i
b = n * (n + 1) // 2
print(a)
print(b)

# Задание 8
n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
count = 0
for i in range(1, n + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print("Было введено %d цифр %d" % (count, d))

# Задание 9

n = int(input('Введите число: '))
max_s = 0
max_m = 0
while n != 0:
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > max_s:
        max_s = s
        max_m = m
    n = int(input('Введите число: '))
print('У числа ', max_m, 'максимальная сумма цифр:', max_s)
