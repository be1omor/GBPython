# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

n = int(input("Введите число: "))
num1 = n/100
num2 = n%100/10
num3 = n%10
res = (int(num1)+int(num2)+int(num3))
print (res)