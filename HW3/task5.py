"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве
"""

from random import randint

origin = []
i = 0
temp = 0
min = [0, 0]
length = int(input('Введите длину массива: '))

for i in range(length):
    temp = randint(-100, 100)
    origin.append(temp)

print('Оригинальный массив: ', origin)
i = 0

for i in range(length):
    if min[0] > origin[i]:
        min[0] = origin[i]
        min[1] = i
        i += 1
    else:
        i += 1

print('Наименьший элементв массиве: {}. Его индекс: {}'.format(min[0], min[1]))
