# Задание 1

import random

a = [random.randint(-100, 100) for i in range(10)]
print(a)


def my_func(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        print(a)


my_func(a)

print(f'Список по убыванию: {a}')

# Задание 2

import random

n = 10
lst = [round(random.uniform(0, 50), 2) for i in range(n)]
print(lst)


def list_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        list_sort(left)
        list_sort(right)

        i = j = k = 0
        left_size = len(left)
        right_size = len(right)

        while i < left_size and j < right_size:
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < left_size:
            lst[k] = left[i]
            i += 1
            k += 1
        while j < right_size:
            lst[k] = right[j]
            j += 1
            k += 1


list_sort(lst)
print(lst)

# Задание 3

import random
import statistics

numb = [random.randint(1, 100) for i in range(10)]


def median(n):
    a = len(n) // 2
    n.sort()
    if not len(n) % 2:
        return (n[a - 1] + n[a]) / 2
    return n[a]


print(numb)
print(median(numb[:]))
print(statistics.median(numb[:]))
