# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. Счастливым 
# билетом называют такой билет с шестизначным номером, где сумма первых 
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – 
# счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

a = int(input('Введите шестизначное число: '))
summ1 = 0
summ2 = 0
i = 0
b = 0
c = 0
while a > 0:
    if i < 3:
        b = a % 10
        summ1 = summ1 + b
        a = a // 10
    else:
        c = a % 10
        summ2 = summ2 + c
        a = a // 10
    i=i+1
print (f'Сумма первых трех чисел: {summ2}')
print (f'Сумма вторых трех чисел: {summ1}')
if summ1 == summ2: print('yes')
else: print('no')
