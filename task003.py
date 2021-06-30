# Задание 1
a = [0]*8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j-2] += 1
i = 0
while i < len(a):
    print(i+2, ' - ', a[i])
    i += 1

# Задание 2
import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Первый массив {r}')
index_even = []

for n in r:
    if n % 2 == 0:
        index_even.append(r.index(n))

print(f'Индексы чётных элементов первого массива: {index_even}')

# Задание 3
from random import random
N = 15
arr = [0]*N
for i in range(N):
    arr[i] = int(random()*100)
    print(arr[i], end=' ')
print()
mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('arr[%d]=%d arr[%d]=%d' % (imn+1, mn, imx+1, mx))
arr[imn], arr[imx] = arr[imx], arr[imn]

for i in range(15):
    print(arr[i], end=' ')
print()

# Задание 4
from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
max_frq = 1
for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')

# Задание 5
from random import random

N = 15
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])

# Задание 6
from random import random
n = 10
a = [0] * n
for i in range(n):
    a[i] = int(random()*50)
    print('%3d' % a[i], end='')
print()
min_id = 0
max_id = 0
for i in range(1, n):
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i
print(a[min_id], a[max_id])
if min_id > max_id:
    min_id, max_id = max_id, min_id
summa = 0
for i in range(min_id+1, max_id):
    summa += a[i]
print(summa)

# Задание 7
from random import randint
array = [randint(1, 20) for i in range(10)]
print(array)
min1 = min(array)
array.remove(min1)
min2 = min(array)
print(min1)
print(min2)

# Задание 8
m = 5
num = 4
a = []
for i in range(num):
    b = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(m - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

for i in a:
    print(i)

# Задание 9
from random import random

m = 10
num = 5
a = []
min_value = 200
for i in range(num):
    b = []
    for j in range(m):
        n = int(random() * min_value)
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

mx = -1
print('---')
for j in range(m):
    mn = min_value
    for i in range(num):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
    print(mn, end=' ')
print("\nМаксимальный среди минимальных: ", mx)





