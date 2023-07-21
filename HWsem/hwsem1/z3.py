# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и 
# получали билет с номером.

# Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех 
# цифр равна сумме последних трех.

# Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6.

# Вам требуется написать программу, 
# которая проверяет счастливость билета с номером n 
# и выводит на экран yes или no.

n = int(input())
a = n // 100000 + n % 100000 //10000 + n % 10000 // 1000
b = n % 1000 // 100 + n % 100 // 10 + n % 10
if a == b:
    print('yes')
else:
    print('no')