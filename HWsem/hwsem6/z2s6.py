# Задача 32: Определить индексы 
# элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше 
# заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

# Вариант 1 (с вводом чисел с клавиатуры).
min = 4
max = 6
list_1 = [index for index, value in enumerate(input().split()) if min <= int(value) <= max]
print(list_1)

# Вариант 2.
# list_1 = [3, 4, 2, 5, 7]
# list_1 = [int(i) for i in input().split()]
# ind = []
# for i in range(len(list_1)):
#     if min <= list_1[i] <= max:
#         ind.append(i)
# print(*ind)
