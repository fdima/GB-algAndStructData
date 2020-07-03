"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = []
string = []
summ = 0

# filling the matrix
for i in range(5):

    string.clear()

    for z in range(3):
        temp = int(input('Enter some natural number >> '))
        string.append(temp)

    temp2 = string[::1]
    matrix.append(temp2)

# counting the sum of each string
for i in range(len(matrix)):

    for z in range(len(matrix[i])):
        summ += matrix[i][z]

    matrix[i].append(summ)
    summ = 0

# printing the matrix
for i in range(len(matrix)):
    print(matrix[i])
