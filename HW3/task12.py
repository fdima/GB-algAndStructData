"""
Задана матрица неотрицательных чисел.
Посчитать сумму элементов в каждом столбце.
Определить, какой столбец содержит максимальную сумму
"""

from random import randint

matrix = []
string = []
summ = []

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

# finding sum of each column
for i in range(width):

    temp = 0

    for z in range(len(matrix)):
        temp += matrix[z][i]

    summ.append(temp)

print('summ = ', summ)

max = summ[0]
index = 0

# findimg column with max sum
for u in range(len(summ)):
    if max <= summ[u]:
        max = summ[u]
        index = u

print('Max sum in {}th column and it is: {}'.format(index+1, max))
