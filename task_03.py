# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности

import os
import random as r
def clear(): return os.system('cls')


clear()


n = int(input('Введите число -> '))
list = [r.randint(0, n) for i in range(10)]
print(list)
list_num=[]
for i in list:
    if i not in list_num:
        list_num.append(i)
print(list_num)