# По данному целому неотрицательному n 
# вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

n = int(input('Введите число: '))
if (n < 0):
    print ("Число отрицательное")

elif (n == 0) or (n == 1):
    print ("Факториал равен 1")

else:
    count = 2
    fact = 1
    while (count <= n):
        fact = fact*count
        count = count + 1
    print ("Факториал равен:")
    print (fact)

# n = int(input("Введите число n: "))
# i = 1
# res = 1
# while i<=n:
#     res *=i
#     i+=1
# print(res)