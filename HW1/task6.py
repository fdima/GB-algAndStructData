# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он
# разносторонним, равнобедренным или равносторонним.

input_str = input('Введите 3 длины отрезка через пробел: ')

numbers = tuple(map(float, input_str.split(' ')))
set_d = set(numbers)
max_d = max(numbers)
less_sum = sum(numbers) - max_d

if max_d < less_sum:
    set_len = len(set_d)

    if set_len == 1:
        print("Треугольник равносторонний")
    elif set_len == 2:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник невозможен")
