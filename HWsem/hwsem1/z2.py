# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали n журавликов.

# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

# Выведите кортеж из количества журавликов, 
# сделанных Петей, Катей и Сережей.

n = int(input())
n1 = n // 6
n2 = n // 6
n3 = (n // 6) * 4
print(n1, n3, n2)

