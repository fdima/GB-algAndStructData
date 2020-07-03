"""
Вводятся пять вещественных чисел.
Записать в первый столбец матрицы целую часть чисел,
во второй - дробную часть, приведенную к пятизначному целому,
в третий столбец - знак числа: 0 для положительных чисел и 1 - для отрицательных.

Например, если вводится число 3.234093, то
в первой ячейке строки присваивается 3,
второй присваивается 23409,
а третьей - число 0
"""

origin = []
matrix = []
string = []
integer = 0
fraction = 0
sign = 0

for i in range(5):
    temp = input("Enter some float number >> ")
    origin.append(temp)

for i in range(len(origin)):

    temp = []
    string.clear()

    if origin[i][0] == '-':
        sign = 1

        temp = origin[i].split('.')

        for x in range(len(temp[0])):
            integer = temp[0][1::1]

        for z in range(len(temp[1])):
            fraction = temp[1][0:5:1]
    else:
        sign = 0

        temp = origin[i].split('.')

        for x in range(len(temp[0])):
            integer = temp[0][::1]

        for z in range(len(temp[1])):
            fraction = temp[1][0:5:1]

    string.append(integer)
    string.append(fraction)
    string.append(sign)
    temp = []
    temp = string[::1]
    matrix.append(temp)

for y in range(len(matrix)):
    print(matrix[y])