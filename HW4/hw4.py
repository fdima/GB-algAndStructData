# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
#
# ----Проверка скорости и разброса по времени алгоритма формирования списка-----
# ----Тест показал, что for работает немного лучше при 3х элементах в списке----
# ----И значительное замедление, а так же увеличение стандартндартной-----------
# ----ошибки при увеличении элементов списка до 5-------------------------------
# ----Сложность алгоритма for похожа на O(n), comprehension тоже должен---------
# ----иметь сложность O(n), однако из-за оптимизации прирост значительно ниже---
# ----Результаты после кода-----------------------------------------------------

import timeit
import statistics as st
import random

for n_iter in [5, 10, 20, 50]:
    def find_min_for():
        lst = [[random.randint(-10, 11) for _ in range(3)] for _ in range(5)]
        lst_t = list(zip(*lst))
        lst_min = []

        for i in lst_t:
            lst_min.append(min(i))

        return max(lst_min)

    def find_min_compr():
        lst = [[random.randint(-10, 11) for _ in range(3)] for _ in range(3)]
        lst_min = [min(i) for i in list(zip(*lst))]
        return max(lst_min)

    time_for = [round(timeit.timeit('find_min_for()', setup='from __main__ import find_min_for', number=100000), 4)
                for _ in range(n_iter)]
    time_compr = [round(timeit.timeit('find_min_compr()', setup='from __main__ import find_min_compr',
                                      number=100000), 4) for _ in range(n_iter)]

    print(f'Количество итераций = {n_iter}\n')
    print(f'Проверка алгоритма через for:\n'
          f'Среднне значение: {round(st.mean(time_for), 4)}  '
          f'Стандартное отклонение: {round(st.stdev(time_for), 6)}\n'
          f'\nПроверка алгоритма через comprehension:\n'
          f'Среднне значение: {round(st.mean(time_compr), 4)}  '
          f'Стандартное отклонение: {round(st.stdev(time_compr), 6)}')
    print('==========================================')

# ===3 элемета в списке=====================
# Количество итераций = 5
#
# Проверка алгоритма через for:
# Среднне значение: 1.1905  Стандартное отклонение: 0.018078
#
# Проверка алгоритма через comprehension:
# Среднне значение: 1.195  Стандартное отклонение: 0.063446
# ==========================================
# Количество итераций = 10
#
# Проверка алгоритма через for:
# Среднне значение: 1.1783  Стандартное отклонение: 0.037442
#
# Проверка алгоритма через comprehension:
# Среднне значение: 1.1993  Стандартное отклонение: 0.032616
# ==========================================
# Количество итераций = 20
#
# Проверка алгоритма через for:
# Среднне значение: 1.211  Стандартное отклонение: 0.044827
#
# Проверка алгоритма через comprehension:
# Среднне значение: 1.2526  Стандартное отклонение: 0.078637
# ==========================================
# Количество итераций = 50
#
# Проверка алгоритма через for:
# Среднне значение: 1.232  Стандартное отклонение: 0.083393
#
# Проверка алгоритма через comprehension:
# Среднне значение: 1.2344  Стандартное отклонение: 0.070766
# ==========================================
# Количество итераций = 100
#
# Проверка алгоритма через for:
# Среднне значение: 1.2293  Стандартное отклонение: 0.082059
#
# Проверка алгоритма через comprehension:
# Среднне значение: 1.2465  Стандартное отклонение: 0.080712
# ==========================================

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ===5 элеметов в списке====================
# Количество итераций = 5
#
# Проверка алгоритма через for:
# Среднне значение: 1.9549  Стандартное отклонение: 0.057136
#
# Проверка алгоритма через comprehension:
# Среднне значение: 1.2816  Стандартное отклонение: 0.035557
# ==========================================
# Количество итераций = 10
#
# Проверка алгоритма через for:
# Среднне значение: 1.9328  Стандартное отклонение: 0.041216
#
# Проверка алгоритма через comprehension:
# Среднне значение: 1.2446  Стандартное отклонение: 0.03389
# ==========================================
# Количество итераций = 20
#
# Проверка алгоритма через for:
# Среднне значение: 1.983  Стандартное отклонение: 0.152548
#
# Проверка алгоритма через comprehension:
# Среднне значение: 1.2561  Стандартное отклонение: 0.067123
# ==========================================
# Количество итераций = 50
#
# Проверка алгоритма через for:
# Среднне значение: 2.0401  Стандартное отклонение: 0.123852
#
# Проверка алгоритма через comprehension:
# Среднне значение: 1.3379  Стандартное отклонение: 0.109948
# ==========================================