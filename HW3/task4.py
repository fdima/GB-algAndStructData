"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

origin = []
i = 0
maxindex = 0
maxnumber = 0
length = int(input(('Введите длину массива >> ')))

for i in range(length):
    temp = randint(1, 99)
    origin.append(temp)
    i += 1

print('Оригинальный массив: ', origin)

i = 0

while i < length:
    temp = origin.count(origin[i])

    if temp > maxindex:
        maxnumber = origin[i]
        maxindex = temp
        i += 1
    else:
        i += 1

print('Число {} встречается {} раз'.format(maxnumber, maxindex))
