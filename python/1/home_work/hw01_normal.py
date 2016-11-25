#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License"


# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
def max_digit(num):
    assert isinstance(num, int)
    maximum = float("-Inf")
    for digit in str(num):
        digit = int(digit)
        if digit > maximum:
            maximum = digit
    return maximum


num = 9870435012938745
yet_another_max = int(max(list(str(num))))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.

# Уже сделано в файле hw01_easy.py


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4
def find_roots(a, b, c):
    dis = b ** 2 - 4 * a * c
    try:
        root1 = (-b - sqrt(dis))/(2 * a)
        root2 = (-b + sqrt(dis))/(2 * a)
    except ValueError:
        # Корни - комплексные числа
        root1 = (-b - complex(sqrt(-dis))) / (2 * a)
        root2 = (-b + complex(sqrt(-dis))) / (2 * a)

    return root1, root2
