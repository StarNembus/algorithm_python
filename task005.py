# Задание 1
import collections

while True:
    try:
        n = int(input('Введите количество компаний: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

companies = collections.defaultdict()
earnings = collections.deque()
unprof_c = collections.deque()
all_profit = 0
QUARTER = 4

for i in range(n):
    name = input(f'\nВведите название {i + 1}й компании: ')
    profit = 0
    q = 1
    while q <= QUARTER:
        try:
            profit += float(input(f'Введите прибыль за {q}й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        q += 1
    companies[name] = profit
    all_profit += profit

mid_profit = all_profit / n
for i, item in companies.items():
    if item >= mid_profit:
        earnings.append(i)
    else:
        unprof_c.append(i)
print(f'Средняя прибыль для всех компаний составила: {mid_profit}')
print(f'Прибыль выше среднего у {len(earnings)} компании:')
for name in earnings:
    print(name)
print(f'Прибыль ниже среднего у {len(unprof_c)} компании:')
for name in unprof_c:
    print(name)

# Задание 2

from collections import defaultdict
from collections import deque


def my_func(string):
    a = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        a += table[num[i]] * 16 ** i
    return a


def my_func1(b):
    num = deque()
    while b > 0:
        d = b % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        b //= 16
    num.reverse()
    return list(num)


signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for k in signs:
    table[k] += counter
    counter += 1

num_1 = my_func(input('Первое число в 16-м формате: ').upper())
num_2 = my_func(input('Второе число в 16-м формате: ').upper())

print(f'Сумма чисел: {my_func1(num_1 + num_2)}')
print(f'Произведение чисел: {my_func1(num_1 * num_2)}')
