# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from math import pi
import os
def clear(): return os.system('cls')
clear()

n = int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {n} равно {round(pi, n)}')