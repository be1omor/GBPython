# Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)

list_number = [1, 10, 2, 3, 7, 9, 12, 0, 5, 7, 8]
max_num = list_number[0]
for el in list_number:
    if el == 0:
        print(max_num)
        break
    elif el > max_num:
        max_num = el