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

# list_1 = [int(i) for i in input().split]
# почему не работает строка? >_<
list_1 = [3, 4, 2, 5, 7]
min = 4
max = 6
ind = []
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        a = i
        ind.append(a)
print(*ind)