"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
"""

from random import randint

origin = []
length = int(input('Enter the length of original array >> '))

for z in range(length):
    temp = randint(1, 500)
    origin.append(temp)

result = []
max = [origin[0], 0]
min = [origin[0], 0]

for i in range(length):
    if origin[i] >= max[0]:
        max[0] = origin[i]
        max[1] = i
    elif origin[i] <= min[0]:
        min[0] = origin[i]
        min[1] = i
    else:
        continue

print(origin)
print(max)
print(min)

origin[min[1]] = max[0]
origin[max[1]] = min[0]
print(origin)
