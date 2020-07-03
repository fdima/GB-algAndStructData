"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9
"""

origin = []
result = []
i = 2
j = 0
N = 10

for z in range(99):
    origin.append(i)
    i += 1

print('Оригинальный массив: ', origin)
i = 2

while i < N:
    temp = []
    for j in range(len(origin)):
        if origin[j] % i == 0:
            temp.append(origin[j])
            j += 1
        else:
            j += 1

    i += 1
    result.append(temp)

for z in range(len(result)):
    print('Числа кратные {}: {}'.format((z + 2), result[z]))
