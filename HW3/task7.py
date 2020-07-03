"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

from random import randint

origin = []
length = int(input('Enter the length of original array >> '))

for z in range(length):
    temp = randint(1, 100)
    origin.append(temp)

print('Original array: ', origin)

min1 = origin[0]

for i in range(len(origin)):
    if origin[i] <= min1:
        min1 = origin[i]
    else:
        continue

origin.remove(min1)

min2 = origin[0]

for i in range(len(origin)):
    if origin[i] <= min2:
        min2 = origin[i]
    else:
        continue

print('Min-1: ', min1)
print('Min-2: ', min2)
