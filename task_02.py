# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

import os
def clear(): return os.system('cls')
clear()

n = int(input('Введите число -> '))
num_list=[]
num=n
i=2
while i <= n:
    if n%i==0:
        num_list.append(i)
        n//=i
        i=2
    else:
        i+=1
print (f"Простые множители числа{num} -> {num_list}")