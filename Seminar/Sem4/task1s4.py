# 25. Напишите программу, которая принимает 
# на вход строку, и отслеживает, сколько раз 
# каждый символ уже встречался. 
# Количество повторов добавляется к символам с 
# помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

input_string = input("Введите строку").split()
dict_string = {}
out_string = ""
for el in input_string:
    if el not in dict_string:
        #print(el)
        out_string += f"{el} "
    else:
        #print(el, dict_string[el])
        out_string += f"{el}_{dict_string[el]} "
    dict_string[el] = dict_string.get(el, 0) + 1

print(out_string)