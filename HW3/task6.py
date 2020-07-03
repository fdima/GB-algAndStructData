"""
В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать
"""

from random import randint

origin = []
length = int(input('Enter the length of original array >> '))

for z in range(length):
    temp = randint(1, 500)
    origin.append(temp)

print('Original list: ', origin)

result = []
summ = 0
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

if min[1] < max[1]:
    result = origin[min[1]+1:max[1]:1]
else:
    result = origin[max[1]+1:min[1]:1]

print('Result list: ', result)

for z in range(len(result)):
    summ += result[z]

print('Required sum: ', summ)
