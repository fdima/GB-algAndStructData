"""
Найти максимальный элемент каждого столбца матрицы
"""

from random import randint

matrix = []
string = []
max = []

width = int(input('Enter width of the matrix >> '))
height = int(input('Enter height of the matrix >> '))
temp = 0

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

# finding max of each column
for i in range(width):
    temp = 0

    for z in range(len(matrix)):
        if temp < matrix[z][i]:
            temp = matrix[z][i]
        else:
            continue

    max.append(temp)

print('max = ', max)
