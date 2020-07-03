"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа
"""

from random import randint

length = int(input('Enter the length of original list >>> '))
origin = []
result = []
i = 0

for z in range(length):
    temp = randint(1, 100)
    origin.append(temp)

print('Оригинальный массив: ', origin)

while i < length:
    if origin[i] % 2 == 0:
        result.append(i)
        i += 1
    else:
        i += 1

print('Массив с индексами чётных чисел: ', result)
