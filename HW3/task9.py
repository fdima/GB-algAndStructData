"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы
"""

from random import randint

matrix = []
string = []
min = []

width = int(input('Enter width of the matrix >> '))
height = int(input('Enter height of the matrix >> '))
temp = 51

# filling the matrix
for i in range(height):

    string.clear()

    for z in range(width):
        temp = randint(1, 50)
        string.append(temp)

    temp2 = string[::1]
    matrix.append(temp2)

# printing the matrix
for i in range(len(matrix)):
    print(matrix[i])

# finding min of each column
for i in range(width):
    temp = 51

    for z in range(len(matrix)):
        if temp > matrix[z][i]:
            temp = matrix[z][i]
        else:
            continue

    min.append(temp)

print('min = ', min)

maxmin = 0

# finding max from [min]
for z in range(len(min)):

    if maxmin < min[z]:
        maxmin = min[z]
    else:
        continue

print('Max of [min] = ', maxmin)
