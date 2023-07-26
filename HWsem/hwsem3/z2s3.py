# Требуется найти в массиве list_1 
# самый близкий по величине элемент к 
# заданному числу k и вывести его.

list_1 = [1, 12, 6, 7, 8, 15]
k = 11

number=0
for i in range(len(list_1)):
    if (k-list_1[i])<=k-number and k-list_1[i]>=0:
        number=i
print(list_1[number])
